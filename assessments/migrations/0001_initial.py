# Generated by Django 2.1.2 on 2018-11-25 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        ('questionnaires', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assessments', to='clients.Client')),
                ('qre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assessments', to='questionnaires.Qre', verbose_name='questionnaire')),
            ],
            options={
                'ordering': ('-created', 'name'),
            },
        ),
    ]
