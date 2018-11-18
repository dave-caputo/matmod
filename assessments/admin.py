from django.contrib import admin
from django.utils.html import format_html

from answers.models import Answer

from .models import Assessment

# @admin.register(Answer)
# class AnswerAdmin(admin.ModelAdmin):
#     pass


@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'qre', 'answers', 'status',
                    'score', 'maximum_score']

    def answers(self, obj):
        answers = (
            obj.answers
            .prefetch_related(
                'question__section',
            ).order_by(
                'question__section',
                'question__order'
            )
        )
        answer_rows = ''.join([
            f'<tr><td><span style="display:block">Section: {answer.question.section}</td>'
            f'<td>Q{answer.question.order + 1}</td><td>{answer.answer}</td><td>{answer.score}</td></tr>'
            for answer in answers
        ])

        return format_html(
            '<table><thead><tr><th>Section</th><th>Question</th><th>Answer</th><th>Score</th></thead><tbody>' +
            answer_rows + '</tbody></table>'
        )

    def status(self, obj):
        return 'Pending' if obj.is_pending else 'Completed'

    def score(self, obj):
        return obj.score

    def maximum_score(self, obj):
        return Answer.ANSWER_CHOICES[-1][0] * obj.answers.count()
