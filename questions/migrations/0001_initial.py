# Generated by Django 2.1.3 on 2018-11-30 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sections', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('question', models.TextField()),
                ('weight', models.DecimalField(decimal_places=1, default=1, max_digits=2)),
                ('choice_text_1', models.TextField(blank=True)),
                ('choice_text_2', models.TextField(blank=True)),
                ('choice_text_3', models.TextField(blank=True)),
                ('choice_text_4', models.TextField(blank=True)),
                ('choice_text_5', models.TextField(blank=True)),
                ('max_score', models.DecimalField(decimal_places=1, default=5, max_digits=5)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='sections.Section')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
    ]
