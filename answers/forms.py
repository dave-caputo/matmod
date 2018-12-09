from django import forms

from .models import Answer


class AnswerForm(forms.ModelForm):
    target = forms.CharField(required=True, label='Target', widget=forms.TextInput(attrs={'hidden': True}))
    answer = forms.CharField(required=True, label='Current', widget=forms.TextInput(attrs={'hidden': True}))

    class Meta:
        model = Answer
        fields = ['target', 'answer']
