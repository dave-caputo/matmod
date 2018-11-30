from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=55, unique=True)
    org = models.ForeignKey(
        'orgs.Org',
        related_name='clients',
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
