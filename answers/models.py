from django.db import models

from questions.models import Questionnaire, Question


# Create your models here.
class AnswerSet(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    name = models.CharField(max_length=55)


    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Answer(models.Model):

    ANSWER_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    ]
    answerset = models.ForeignKey(AnswerSet, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.IntegerField(choices=ANSWER_CHOICES, blank=True, null=True)

    def __str__(self):
        return f'{self.answerset}: Q{self.question.order  + 1} = {self.answer}'

    class Meta:
        ordering = ('question__order',)
