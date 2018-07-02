from django.contrib import admin
from django.utils.html import format_html

from .models import Qre


# @admin.register(Question)
# class QuestionAdmin(admin.ModelAdmin):
#     pass


@admin.register(Qre)
class QreAdmin(admin.ModelAdmin):
    list_display = ['name', 'questions']

    def questions(self, obj):
        html = []
        for s in obj.sections.all():
            html.append(
                '<span style="display:block"><strong>'
                f'{s}</strong></span>')

            qns_list = ''.join(
                [f'<span style="display:block">'
                 f'<a href="/admin/questionnaires/question/{q.id}/change/"'
                 ' target="_blank">'
                 f'{q.order + 1}. {q.question}</a></span>'
                 for q in s.questions.all()]
            )
            html.append(qns_list)

        return format_html(''.join(html))


# @admin.register(Section)
# class SectionAdmin(admin.ModelAdmin):
#     list_display = ['get_str', 'qre']

#     def get_str(self, obj):
#         return obj
#     get_str.short_description = 'section'
