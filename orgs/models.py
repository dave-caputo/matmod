from django.db import models

from .countries import COUNTRIES


class Org(models.Model):
    name = models.CharField(max_length=55)
    country = models.CharField(max_length=255, choices=COUNTRIES, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
