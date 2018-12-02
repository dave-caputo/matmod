from django import forms

from .models import Qre


class QreForm(forms.ModelForm):

    class Meta:
        model = Qre
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter name'}),
            'org': forms.HiddenInput(),
        }
