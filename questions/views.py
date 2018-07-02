from django.views import generic
from django.urls import reverse

from .forms import QuestionForm
from .models import Question


class QuestionCreateView(generic.CreateView):
    form_class = QuestionForm
    model = Question
    template_name = 'questions/create.html'

    def get_success_url(self):
        return reverse('sections:create', kwargs={
            'qre_pk': self.kwargs['qre_pk'],
            'section_pk': self.kwargs['section_pk']
        })
