# Generated by Django 2.1.2 on 2018-11-12 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Qre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
            ],
            options={
                'verbose_name': 'questionnaire',
                'ordering': ('name',),
            },
        ),
    ]
