from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

from .countries import COUNTRIES


class Org(MPTTModel):
    name = models.CharField(max_length=55)
    country = models.CharField(max_length=255, choices=COUNTRIES, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = 'name'

    def __str__(self):
        return self.name
