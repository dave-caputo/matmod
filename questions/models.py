from django.db import models
from ordered_model.models import OrderedModel


# Create your models here.
class Questionnaire(models.Model):
    name = models.CharField(max_length=55)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Question(OrderedModel):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f'{self.order  + 1}. {self.text}'

    class Meta(OrderedModel.Meta):
        pass
