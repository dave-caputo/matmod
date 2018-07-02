from django.db import models
from ordered_model.models import OrderedModel

from sections.models import Section


# Create your models here.
class Qre(models.Model):
    name = models.CharField(max_length=55)

    class Meta:
        ordering = ('name',)
        verbose_name = 'questionnaire'

    def __str__(self):
        return self.name
