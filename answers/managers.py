from django.db import models
from django.db.models import Sum


class AnswerTotalsManager(models.Manager):

    def totals(self):

        return self.get_queryset() \
            .aggregate(total_score=Sum('score'))
