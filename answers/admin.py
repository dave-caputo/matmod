from django.contrib import admin

from .models import Answer, AnswerSet

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass


@admin.register(AnswerSet)
class AnswerSetAdmin(admin.ModelAdmin):
    pass

