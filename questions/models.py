from django.db import models

from ordered_model.models import OrderedModel


class Question(OrderedModel):
    section = models.ForeignKey('sections.Section',
                                related_name='questions',
                                on_delete=models.CASCADE)
    question = models.TextField()
    order_with_respect_to = 'section'

    def __str__(self):
        return f'{self.order  + 1}. {self.question}'

    class Meta(OrderedModel.Meta):
        pass
