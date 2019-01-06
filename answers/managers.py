from django.db import models
from django.db.models import Count, ExpressionWrapper, F, Sum
from django.db.models.functions import Coalesce


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
                answer_count=Count('answer'),
            )
            .annotate(
                score=ExpressionWrapper(
                    Coalesce(Sum('score') / F('answer_count'), 0),
                    output_field=models.DecimalField(),
                ),
                target_score=ExpressionWrapper(
                    Coalesce(Sum('target_score') / F('answer_count'), 0),
                    output_field=models.DecimalField(),
                ),
                max_score=ExpressionWrapper(
                    Coalesce(Sum('question__max_score') / F('answer_count'), 0),
                    output_field=models.DecimalField(),
                ),
            )
            .annotate(
                maturity=F('score') / F('max_score') * 100,
                target_score_pc=F('target_score') / F('max_score') * 100,
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
