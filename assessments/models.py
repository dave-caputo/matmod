from django.db import models

from answers.models import Answer


# Create your models here.
class Assessment(models.Model):
    qre = models.ForeignKey('questionnaires.Qre',
                            verbose_name='questionnaire',
                            related_name='assessments',
                            on_delete=models.CASCADE)
    client = models.ForeignKey('clients.Client',
                               related_name='assessments',
                               on_delete=models.CASCADE)
    name = models.CharField(max_length=55)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created', 'name',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        created = True if not self.pk else False
        super().save(*args, **kwargs)

        # Create answers for new assessment
        if created:
            for question in self.qre.get_questions():
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
        return self.answers.totals['score']

    @property
    def max_score(self):
        return self.answers.totals['max_score']

    @property
    def score_pc(self):
        return self.score / self.max_score * 100
