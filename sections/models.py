from django.db import models

from ordered_model.models import OrderedModel


class Section(OrderedModel):
    qre = models.ForeignKey('questionnaires.Qre',
                            verbose_name='questionnaire',
                            on_delete=models.CASCADE,
                            related_name='sections')
    name = models.CharField(max_length=55)
    order_with_respect_to = 'qre'

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return f'{self.order + 1}. {self.name}'
