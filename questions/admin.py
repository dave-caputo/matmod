from django.contrib import admin
from .models import Question, Questionnaire


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    pass
