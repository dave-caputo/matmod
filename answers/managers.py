from django.db import models
from django.db.models import Sum, F, Value


class AnswerTotalsManager(models.Manager):

    def totals(self):

        return self.get_queryset() \
            .aggregate(total_score=Sum('score'))

    def section_totals(self):

        return self.get_queryset() \
            .select_related('question__section') \
            .order_by('question__section') \
            .values(
                order=F('question__section__order') + 1,
                name=F('question__section__name')) \
            .annotate(
                answers=Sum('answer'),
                score=Sum(
                    F('answer') * F('weight'),
                    output_field=models.DecimalField()
                ),
                max_score=Sum(
                    Value(self.model.ANSWER_CHOICES[-1][0]) * F('weight'),
                    output_field=models.DecimalField()
                )) \
            .annotate(
                score_pc=F('score') / F('max_score') * 100
        )
