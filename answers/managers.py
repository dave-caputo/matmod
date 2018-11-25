from django.db import models
from django.db.models import F, Sum


class AnswerTotalsManager(models.Manager):

    @property
    def section_totals(self):

        return (
            self.get_queryset()
            .select_related('question__section')
            .order_by('question__section')
            .values(
                order=F('question__section__order') + 1,
                name=F('question__section__name')
            )
            .annotate(
                answers=Sum('answer'),
                score=Sum('score', output_field=models.DecimalField()),
                target_score=Sum('target_score', output_field=models.DecimalField()),
                max_score=Sum('question__max_score', output_field=models.DecimalField()),
            )
            .annotate(
                maturity=F('score') / F('max_score') * 100,
                target_score_pc=F('target_score') / F('max_score') * 100
            )
        )

    @property
    def totals(self):
        return (
            self.get_queryset()
            .select_related('question')
            .aggregate(
                score=Sum(
                    F('answer') * F('question__weight'),
                    output_field=models.DecimalField()
                ),
                target_score=Sum(
                    F('target') * F('question__weight'),
                    output_field=models.DecimalField()
                ),
                max_score=Sum(
                    F('question__max_score'),
                    output_field=models.DecimalField()
                ),
            )
        )
