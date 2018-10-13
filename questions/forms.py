from django import forms

from .models import Question


class QuestionForm(forms.ModelForm):

    class Meta:
        fields = ['section', 'question', 'weight', 'min_legend', 'max_legend']
        model = Question
        widgets = {
            'section': forms.HiddenInput(),
        }
