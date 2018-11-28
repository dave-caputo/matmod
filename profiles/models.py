from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_staff = models.BooleanField(
        verbose_name='admin status', default=False,
        help_text='Designates whether the user can log into this admin site.',
    )
    org = models.ForeignKey(
        'orgs.Org', blank=True, null=True, related_name="users",
        on_delete=models.SET_NULL, verbose_name='organisation'
    )
    client = models.ForeignKey(
        'clients.Client', blank=True, null=True, related_name="users", on_delete=models.SET_NULL
    )
