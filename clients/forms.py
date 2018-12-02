from django import forms

from .models import Client


class ClientForm(forms.ModelForm):
    """A representation of a third party who is the subject of questionnaire assessments."""

    class Meta:
        model = Client
        fields = ['name', 'org']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter name'}),
            'org': forms.HiddenInput(),
        }
