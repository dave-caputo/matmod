from django import forms

from .models import Answer


class AnswerForm(forms.ModelForm):
    answer = forms.ChoiceField(
        choices=[(0, 'No response'), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)],
        widget=forms.RadioSelect())
    # question_string = forms.CharField(max_length=255, widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['answer'].required = True

    class Meta:
        model = Answer
        # fields = ['assessment', 'question', 'answer']
        fields = ['id', 'answer']
        widgets = {
            # 'assessment': forms.HiddenInput(),
            # 'question': forms.HiddenInput(),
            # 'question_string': forms.HiddenInput()
        }


# def get_answer_formset():

#     return forms.inlineformset_factory(
#         Answer,
#         form=AnswerForm,
#         # fields=['assessment', 'question', 'answer'],
#         fields=['id', 'answer'],
#         extra=0,
#         max_num=0
#     )


# def get_answer_formset():

#     return forms.modelformset_factory(
#         form=AnswerForm,
#         # fields=['assessment', 'question', 'answer'],
#         # fields=['id', 'answer'],
#         extra=0,
#         max_num=0
#     )
