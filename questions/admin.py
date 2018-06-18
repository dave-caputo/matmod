from django.contrib import admin
from django.utils.html import format_html


from .models import Question, Questionnaire


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ['name', 'questions']

    def questions(self, obj):
        qns_list = ''.join(
            [f'<span style="display:block">'
             f'{q.order + 1}. {q.text}</span>'
             for q in obj.question_set.all()]
        )

        return format_html(qns_list)
