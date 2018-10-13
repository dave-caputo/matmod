from django import forms

from .models import Assessment


class AssessmentForm(forms.ModelForm):

    class Meta:
        fields = ['qre', 'name', 'client']
        model = Assessment
        widgets = {'client': forms.HiddenInput()}
