from django import forms

from .models import Answer


class AnswerForm(forms.ModelForm):
    answer = forms.ChoiceField(
        choices=[(0, 'No response'), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)],
        widget=forms.RadioSelect())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['answer'].required = True

    class Meta:
        model = Answer
        fields = ['answer']
