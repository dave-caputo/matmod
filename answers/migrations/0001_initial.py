# Generated by Django 2.1.3 on 2018-11-30 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assessments', '0001_initial'),
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0)),
                ('target', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0)),
                ('score', models.DecimalField(decimal_places=1, default=0, max_digits=6)),
                ('target_score', models.DecimalField(decimal_places=1, default=0, max_digits=6)),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='assessments.Assessment')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='questions.Question')),
            ],
            options={
                'ordering': ('assessment', 'question__order'),
            },
        ),
    ]
