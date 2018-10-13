from django import forms

from .models import Answer


class AnswerForm(forms.ModelForm):
    answer = forms.ChoiceField(required=True, widget=forms.RadioSelect())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['answer'].choices = [
            (0, 'No response'),
            (1, f'{self.instance.question.min_legend or 1}'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, f'{self.instance.question.max_legend or 5}'),
        ]

    class Meta:
        model = Answer
        fields = ['answer']
