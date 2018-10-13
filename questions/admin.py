from django.contrib import admin

from .models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['get_str', 'get_qre', 'section', 'min_legend', 'max_legend']
    ordering = ['section__qre', 'section__order', 'order']

    def get_str(self, obj):
        return obj
    get_str.short_description = 'question'

    def get_qre(self, obj):
        return obj.section.qre
    get_qre.short_description = 'questionnaire'
