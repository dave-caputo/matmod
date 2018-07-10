from django import forms

from answers.forms import AnswerForm
from answers.models import Answer
from .models import Assessment


class AssessmentForm(forms.ModelForm):

    class Meta:
        fields = ['qre', 'name', 'client']
        model = Assessment
        widgets = {'client': forms.HiddenInput()}


# def get_answers_formset():

#     return forms.inlineformset_factory(
#         Assessment,
#         Answer,
#         form=AnswerForm,
#         extra=0,
#         max_num=0
#     )


def get_answers_formset():

    return forms.modelformset_factory(
        form=AnswerForm,
        model=Answer,
        # fields=['assessment', 'question', 'answer'],
        # fields=['id', 'answer'],
        extra=0,
        max_num=0
    )
