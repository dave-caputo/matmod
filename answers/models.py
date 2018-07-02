from django.db import models


class Answer(models.Model):

    ANSWER_CHOICES = [
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    ]

    assessment = models.ForeignKey('assessments.Assessment',
                                   on_delete=models.CASCADE,
                                   related_name='answers')

    question = models.ForeignKey('questions.Question', on_delete=models.CASCADE)

    answer = models.IntegerField(choices=ANSWER_CHOICES,
                                 blank=True,
                                 null=True,
                                 default=0)

    def __str__(self):
        return f'{self.assessment}: Q{self.question.order  + 1} = {self.answer}'

    class Meta:
        ordering = ('assessment', 'question__order',)
