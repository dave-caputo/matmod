from django.db import models

from questions.models import Question


# Create your models here.
class Qre(models.Model):
    name = models.CharField(max_length=55)
    org = models.ForeignKey(
        'orgs.Org', blank=True, null=True, related_name='qres',
        on_delete=models.SET_NULL, verbose_name='organisation'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'questionnaire'

    def __str__(self):
        return self.name

    def get_questions(self):
        return Question.objects.filter(section__qre=self)
