from django import forms

from .models import Section


class SectionForm(forms.ModelForm):

    class Meta:
        fields = ['qre', 'name']
        model = Section
        widgets = {'qre': forms.HiddenInput()}
