from django import forms

from .models import Question


class QuestionForm(forms.ModelForm):

    class Meta:
        fields = ['section', 'question']
        model = Question
        widgets = {
            'section': forms.HiddenInput(),
        }
