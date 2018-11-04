from django import forms

from crispy_forms.bootstrap import StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, Layout

from .models import Question


class QuestionForm(forms.ModelForm):

    class Meta:
        fields = ['question', 'weight', 'choice_text_1', 'choice_text_2',
                  'choice_text_3', 'choice_text_4', 'choice_text_5', ]
        model = Question
        widgets = {
            'section': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'question_update_form' if self.instance.pk else 'question_create_form'

        # Form layout
        choice_divs = [Div(Field(f'choice_text_{i}', style='height:100px'), css_class='col-md') for i in range(1, 6)]
        self.helper.layout = Layout(
            Div(
                Div(Field('question', style='height:100px;'), css_class='col-md-8'),
                Div('weight', css_class='col-md-4'),
                css_class='row',
            ),
            Div(*choice_divs, css_class='row'),
            Div(
                Div(StrictButton('Update', css_class='btn-primary', css_id='question_update_btn'), css_class='col'),
                css_class='row'
            )
        )
