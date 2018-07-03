from django.db import models
from ordered_model.models import OrderedModel

from questions.models import Question


# Create your models here.
class Qre(models.Model):
    name = models.CharField(max_length=55)

    class Meta:
        ordering = ('name',)
        verbose_name = 'questionnaire'

    def __str__(self):
        return self.name

    def get_questions(self):
        return Question.objects.filter(section__qre=self)
