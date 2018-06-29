from django import forms

from .models import Section


class QreSectionForm(forms.ModelForm):

    class Meta:
        fields = ['qre', 'name']
        model = Section
        widgets = {'qre': forms.HiddenInput()}
