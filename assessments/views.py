from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic

from answers.forms import AnswerForm
from answers.models import Answer
from clients.models import Client

from .forms import AssessmentForm
from .models import Assessment


class AssessmentCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = AssessmentForm
    model = Assessment
    template_name = 'assess/create.html'

    def get_success_url(self):
        return reverse('assess:create', kwargs={'client_pk': self.kwargs['client_pk']})

    def get_initial(self):
        client = get_object_or_404(Client, id=self.kwargs['client_pk'])
        return {'client': client}


class AssessmentListView(LoginRequiredMixin, generic.ListView):
    model = Assessment
    template_name = 'assess/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return (
            qs
            .select_related('client')
            .filter(client__pk=self.kwargs['client_pk'])
        )


class AssessmentDetailView(LoginRequiredMixin, generic.DetailView):
    model = Assessment
    template_name = 'assess/detail.html'

    def get_answers(self):
        """Return a queryset with the assessment answers ordered by section and question."""
        return (
            self.get_object()
            .answers
            .select_related('question__section')
            .order_by('question__section', 'question')
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        ans_qs = self.get_answers()
        context['answer_list'] = ans_qs
        context['client_pk'] = self.kwargs['client_pk']
        context['section_totals'] = self.get_object().answers.section_totals

        return context


class AssessmentCompleteView(AssessmentDetailView):
    template_name = 'assess/complete.html'

    def post(self, request, *args, **kwargs):
        """Save answer formset data."""
        formset = self.get_answers_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
        else:
            formset = self.get_answers_formset()

        return HttpResponseRedirect(
            reverse('assess:detail', kwargs={'client_pk': self.kwargs['client_pk'], 'pk': self.get_object().pk})
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['answer_formset'] = self.get_answers_formset()
        return context

    def get_answers_formset(self, data=None):
        """Return a bound/unbound formset containing a form for each of the assessment answers."""
        AnswerFormSet = forms.modelformset_factory(form=AnswerForm, model=Answer, extra=0, max_num=0)
        return AnswerFormSet(data=data, queryset=self.get_answers())


class AssessmentRenameView(LoginRequiredMixin, generic.UpdateView):
    model = Assessment
    template_name = 'assess/rename.html'
    fields = ['name']

    def get_success_url(self):
        return reverse('assess:rename', kwargs={'client_pk': self.kwargs['client_pk'], 'pk': self.kwargs['pk']})


class AssessmentDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Assessment
    template_name = 'assess/delete.html'

    def get_success_url(self):
        return reverse('clients:detail', kwargs={
            'pk': self.kwargs['client_pk']})
