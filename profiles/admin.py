from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from profiles.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    pass
