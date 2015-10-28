# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schools', '0011_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerStudentTemp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer_score', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('answer_grade', models.CharField(max_length=30, null=True, blank=True)),
                ('double_entry', models.IntegerField(default=0, null=True, blank=True)),
                ('status', models.IntegerField(null=True, blank=True)),
                ('creation_date', models.DateField(auto_now_add=True, null=True)),
                ('last_modified_date', models.DateField(auto_now=True, null=True)),
                ('flexi_data', models.CharField(max_length=30, null=True, blank=True)),
                ('last_modified_by', models.ForeignKey(related_name='temp_last_modified_answer_student', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('question', models.ForeignKey(to='schools.QuestionStudent')),
                ('user1', models.ForeignKey(related_name='temp_user1', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('user2', models.ForeignKey(related_name='temp_user2', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='answerinstitution',
            name='active',
            field=models.IntegerField(default=2, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='answerinstitution',
            name='institution_id',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='answerstudent',
            name='active',
            field=models.IntegerField(default=2, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='answerstudent',
            name='student_id',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
