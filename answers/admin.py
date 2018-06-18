from django.contrib import admin
from django.utils.html import format_html

from .models import Answer, AnswerSet


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass


@admin.register(AnswerSet)
class AnswerSetAdmin(admin.ModelAdmin):
    list_display = ['name', 'questionnaire', 'get_answers']

    def get_answers(self, obj):
        ans_list = [f'<span style="display:block">'
                    f'Q{a.question.order + 1}={a.answer}</span>' for a in
                    obj.answer_set.all()]

        answers = ''.join(ans_list)

        return format_html(answers)
