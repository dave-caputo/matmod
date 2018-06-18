from django.contrib import admin
from django.utils.html import format_html

from .models import Answer, Assessment


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass


@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'questionnaire', 'get_answers', 'status']

    def get_answers(self, obj):
        answers = ''.join(
            ['<span style="display:block">'
             f'<a target="_blank" href="/admin/answers/answer/{a.pk}/change/">'
             f'Q{a.question.order + 1}={a.answer}</span>' for a in
             obj.answers.all()]
        )

        return format_html(answers)

    def status(self, obj):
        return 'Pending' if obj.is_pending else 'Completed'
