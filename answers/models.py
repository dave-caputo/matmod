from django.db import models

from .managers import AnswerTotalsManager


class Answer(models.Model):

    ANSWER_CHOICES = [
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    ]

    objects = AnswerTotalsManager()

    assessment = models.ForeignKey('assessments.Assessment', on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey('questions.Question', on_delete=models.CASCADE)
    answer = models.IntegerField(choices=ANSWER_CHOICES, default=0)
    score = models.DecimalField(max_digits=6, decimal_places=1, default=0)

    class Meta:
        ordering = ('assessment', 'question__order',)

    def __str__(self):
        return (
            f'{self.assessment}: Q{self.question.order  + 1} '
            f'{self.question.question} = {self.answer}'
        )

    def save(self, *args, **kwargs):
        self.score = self.answer * self.question.weight
        super().save(*args, **kwargs)
