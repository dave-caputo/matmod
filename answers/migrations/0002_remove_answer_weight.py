# Generated by Django 2.0.6 on 2018-07-12 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('answers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='weight',
        ),
    ]
