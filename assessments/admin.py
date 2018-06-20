from django.contrib import admin
from django.utils.html import format_html

from .models import Answer, Assessment


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass


@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'qre', 'answers', 'status',
                    'score', 'maximum_score']

    def answers(self, obj):
        answers = ''.join(
            ['<span style="display:block">'
             '<a target="_blank"'
             f' href="/admin/assessments/answer/{a.pk}/change/">'
             f'Q{a.question.order + 1}={a.answer}</span>' for a in
             obj.answers.select_related('question__qre').all()]
        )

        return format_html(answers)

    def status(self, obj):
        return 'Pending' if obj.is_pending else 'Completed'

    def score(self, obj):
        return obj.score

    def maximum_score(self, obj):
        return Answer.ANSWER_CHOICES[-1][0] * obj.answers.count()
