from django.shortcuts import get_object_or_404
from django.views import generic
from django.urls import reverse

from sections.models import Section
from .forms import QuestionForm
from .models import Question


class QuestionCreateView(generic.CreateView):
    form_class = QuestionForm
    model = Question
    template_name = 'questions/create.html'

    def get_initial(self):
        section = get_object_or_404(Section, id=self.kwargs['section_pk'])
        return {'section': section}

    def get_success_url(self):
        return reverse('questions:create', kwargs={
            'qre_pk': self.kwargs['qre_pk'],
            'section_pk': self.kwargs['section_pk']
        })


class QuestionListView(generic.ListView):
    model = Question
    template_name = 'questions/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(section__pk=self.kwargs['section_pk'])
