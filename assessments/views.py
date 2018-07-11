from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic

from answers.forms import AnswerForm
from answers.models import Answer
from clients.models import Client
from .forms import AssessmentForm, get_answers_formset
from .models import Assessment


class AssessmentCreateView(generic.CreateView):
    form_class = AssessmentForm
    model = Assessment
    template_name = 'assess/create.html'
    success_url = reverse_lazy('clients:create')

    def get_initial(self):
        client = get_object_or_404(Client, id=self.kwargs['client_pk'])
        return {'client': client}


class AssessmentListView(generic.ListView):
    model = Assessment
    template_name = 'assess/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.select_related('client').filter(
            client__pk=self.kwargs['client_pk'])


class AssessmentDetailView(generic.DetailView):
    model = Assessment
    template_name = 'assess/detail.html'

    def get_answers(self):
        return self.get_object().answers \
            .select_related('question__section') \
            .order_by('question__section', 'question')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        ans_qs = self.get_answers()
        context['answer_list'] = ans_qs
        context['client_pk'] = self.kwargs['client_pk']
        return context


class AssessmentCompleteView(AssessmentDetailView):
    template_name = 'assess/complete.html'

    def post(self, request, *args, **kwargs):

        AnswerFormSet = get_answers_formset()
        # formset = AnswerFormSet(request.POST, instance=self.self_object)
        formset = AnswerFormSet(request.POST, queryset=self.get_answers())
        if formset.is_valid():
            formset.save()
        else:
            # formset = AnswerFormSet(instance=self.get_object)
            formset = AnswerFormSet(queryset=self.get_answers())

        return HttpResponseRedirect(reverse('assess:detail', kwargs={
            'client_pk': self.kwargs['client_pk'],
            'pk': self.get_object().pk
        }))

    def get_answers_formset(self):
        AnswerFormSet = get_answers_formset()
        # return AnswerFormSet(instance=self.object)
        return AnswerFormSet(queryset=self.get_answers())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['answer_formset'] = self.get_answers_formset()
        return context


class AssessmentUpdateView(generic.UpdateView):
    model = Assessment
    template_name = 'assess/update.html'
    fields = ['name']

    def get_success_url(self):
        return reverse('assess:update', kwargs={
            'client_pk': self.kwargs['client_pk'],
            'pk': self.kwargs['pk']})


class AssessmentDeleteView(generic.DeleteView):
    model = Assessment
    template_name = 'assess/delete.html'

    def get_success_url(self):
        return reverse('clients:detail', kwargs={
            'pk': self.kwargs['client_pk']})
