from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=55, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
