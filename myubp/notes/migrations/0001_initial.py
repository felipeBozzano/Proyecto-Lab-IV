# Generated by Django 3.2.9 on 2021-11-06 20:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_note', models.IntegerField()),
                ('id_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_note', to='subjects.subject')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_note', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]