# Generated by Django 2.0.6 on 2018-10-13 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_question_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='max_legend',
            field=models.CharField(blank=True, help_text='Meaning of the answer with the highest score.', max_length=155, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='min_legend',
            field=models.CharField(blank=True, help_text='Meaning of the answer with the lowest score.', max_length=155, null=True),
        ),
    ]