from django.db import models

from ordered_model.models import OrderedModel


class Question(OrderedModel):
    """A model representing a question that belongs to an assessment section."""

    section = models.ForeignKey('sections.Section', related_name='questions', on_delete=models.CASCADE)
    question = models.TextField()
    weight = models.DecimalField(max_digits=2, decimal_places=1, null=True, default=1)
    choice_text_0 = models.TextField(default='No Response', editable=False)
    choice_text_1 = models.TextField(blank=True, max_length=100)
    choice_text_2 = models.TextField(blank=True)
    choice_text_3 = models.TextField(blank=True)
    choice_text_4 = models.TextField(blank=True)
    choice_text_5 = models.TextField(blank=True)

    order_with_respect_to = ('section',)

    class Meta(OrderedModel.Meta):
        """Meta required to inherit from ``OrderedModel.Meta`` (https://github.com/bfirsh/django-ordered-model)."""
        pass

    def __str__(self):
        return f'{self.section.order + 1}.{self.order  + 1}. {self.question}'
