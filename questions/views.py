from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic

from sections.models import Section

from .forms import QuestionForm
from .models import Question


class QuestionCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = QuestionForm
    model = Question
    template_name = 'questions/create.html'

    def get_initial(self):
        initial = super().get_initial()
        initial['section'] = get_object_or_404(Section, id=self.kwargs['section_pk'])
        return initial

    def get_success_url(self):
        return reverse('questions:create', kwargs={
            'qre_pk': self.kwargs['qre_pk'],
            'section_pk': self.kwargs['section_pk']
        })


class QuestionListView(LoginRequiredMixin, generic.ListView):
    model = Question
    template_name = 'questions/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(section__pk=self.kwargs['section_pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qre_pk'] = self.kwargs['qre_pk']
        context['section_pk'] = self.kwargs['section_pk']
        return context


class QuestionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Question
    template_name = 'questions/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qre_pk'] = self.kwargs['qre_pk']
        context['section_pk'] = self.kwargs['section_pk']
        return context


class QuestionMoveView(LoginRequiredMixin, generic.UpdateView):
    """Move section up/down in the qre by updating the order field using the Ordered Model 'up'/'down' methods."""

    model = Question
    fields = []

    def form_valid(self, form):

        direction = self.kwargs.get('direction')  # Accepts str 'up' or 'down'
        self.object = form.save()
        getattr(self.object, direction)()

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('questions:list', kwargs={
            'qre_pk': self.kwargs['qre_pk'],
            'section_pk': self.kwargs['section_pk']
        })


class QuestionUpdateView(LoginRequiredMixin, generic.UpdateView):

    form_class = QuestionForm
    model = Question
    template_name = 'questions/update.html'

    def get_success_url(self):
        kwargs = {
            'qre_pk': self.kwargs['qre_pk'],
            'section_pk': self.kwargs['section_pk'],
            'pk': self.get_object().pk
        }
        return reverse('questions:update', kwargs=kwargs)


class QuestionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Question
    template_name = 'questions/delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qre_pk'] = self.kwargs['qre_pk']
        context['section_pk'] = self.kwargs['section_pk']
        return context

    def get_success_url(self):
        return reverse('sections:detail', kwargs={
            'qre_pk': self.kwargs['qre_pk'],
            'pk': self.kwargs['section_pk'],
        })
