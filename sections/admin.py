from django.contrib import admin

from .models import Section


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['get_str', 'qre']

    def get_str(self, obj):
        return obj
    get_str.short_description = 'section'
