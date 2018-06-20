from django.db import models

from clients.models import Client
from questionnaires.models import Qre, Question


# Create your models here.
class Assessment(models.Model):
    qre = models.ForeignKey(Qre,
                            verbose_name='questionnaire',
                            related_name='assessments',
                            on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=55)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        created = True if not self.pk else False
        super().save(*args, **kwargs)

        # Create answers for new assessment
        if created:
            for question in self.qre.questions.all():
                Answer.objects.create(
                    assessment=self,
                    question=question,
                )

    @property
    def is_pending(self):
        qs = self.answers.filter(answer=0)
        return True if qs.exists() else False

    @property
    def score(self):
        return self.answers.aggregate(total=models.Sum('answer'))['total']


class Answer(models.Model):

    ANSWER_CHOICES = [
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    ]

    assessment = models.ForeignKey(Assessment,
                                   on_delete=models.CASCADE,
                                   related_name='answers')

    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    answer = models.IntegerField(choices=ANSWER_CHOICES,
                                 blank=True,
                                 null=True,
                                 default=0)

    def __str__(self):
        return f'{self.assessment}: Q{self.question.order  + 1} = {self.answer}'

    class Meta:
        ordering = ('assessment', 'question__order',)
