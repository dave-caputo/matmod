from django.contrib import admin

from .models import Org


@admin.register(Org)
class OrgAdmin(admin.ModelAdmin):
    pass
