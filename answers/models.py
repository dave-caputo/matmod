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

    def save(self, *args, **kwargs):
        
        created = True if not self.pk else False
        super().save(*args, **kwargs)
        # Create answerset
        if created:
            for question in self.questionnaire.question_set.all():
                Answer.objects.create(
                    answerset=self,
                    question=question,
                )


class Answer(models.Model):

    ANSWER_CHOICES = [
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    ]

    answerset = models.ForeignKey(AnswerSet, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    answer = models.IntegerField(choices=ANSWER_CHOICES,
                                 blank=True,
                                 null=True,
                                 default=0)

    def __str__(self):
        return f'{self.answerset}: Q{self.question.order  + 1} = {self.answer}'

    class Meta:
        ordering = ('answerset', 'question__order',)
