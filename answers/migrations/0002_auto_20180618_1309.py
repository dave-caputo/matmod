# Generated by Django 2.0.6 on 2018-06-18 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('answers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'ordering': ('answerset', 'question__order')},
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.IntegerField(blank=True, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0, null=True),
        ),
    ]
