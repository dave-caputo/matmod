from django import forms

from .models import Answer


class AnswerForm(forms.ModelForm):
    answer = forms.CharField(required=True, label='Current', widget=forms.TextInput(attrs={'hidden': True}))
    target = forms.CharField(required=True, label='Target', widget=forms.TextInput(attrs={'hidden': True}))

    class Meta:
        model = Answer
        fields = ['answer', 'target']
