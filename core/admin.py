from django.contrib import admin
from django.contrib.sites.models import Site


class CustomAdminSite(admin.AdminSite):
    site_header = Site.objects.get_current().name
