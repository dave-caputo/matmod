from django.db import models
from ordered_model.models import OrderedModel


# Create your models here.
class Qre(models.Model):
    name = models.CharField(max_length=55)

    class Meta:
        ordering = ('name',)
        verbose_name = 'questionnaire'

    def __str__(self):
        return self.name


class Section(OrderedModel):
    qre = models.ForeignKey(Qre,
                            verbose_name='questionnaire',
                            on_delete=models.CASCADE,
                            related_name='sections')
    name = models.CharField(max_length=55)
    order_with_respect_to = 'qre'

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return f'{self.order}. {self.name}'


class Question(OrderedModel):
    qre = models.ForeignKey(Qre,
                            verbose_name='questionnaire',
                            related_name='questions',
                            on_delete=models.CASCADE)

    section = models.ForeignKey(Section,
                                related_name='questions',
                                on_delete=models.CASCADE)

    question = models.TextField()

    def __str__(self):
        return f'{self.order  + 1}. {self.question}'

    class Meta(OrderedModel.Meta):
        pass
