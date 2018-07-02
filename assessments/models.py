from django.db import models


# Create your models here.
class Assessment(models.Model):
    qre = models.ForeignKey('questionnaires.Qre',
                            verbose_name='questionnaire',
                            related_name='assessments',
                            on_delete=models.CASCADE)
    client = models.ForeignKey('clients.Client', on_delete=models.CASCADE)
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
