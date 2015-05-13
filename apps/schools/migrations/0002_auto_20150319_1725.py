# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerInstitution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer_score', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('answer_grade', models.CharField(max_length=30, null=True, blank=True)),
                ('double_entry', models.IntegerField(default=0, null=True, blank=True)),
                ('status', models.IntegerField(null=True, blank=True)),
                ('creation_date', models.DateField(auto_now_add=True, null=True)),
                ('last_modified_date', models.DateField(auto_now=True, null=True)),
                ('flexi_data', models.CharField(max_length=30, null=True, blank=True)),
                ('last_modified_by', models.ForeignKey(related_name='last_modified_answer_institution', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('question', models.ForeignKey(to='schools.Question')),
                ('user1', models.ForeignKey(related_name='user1_answer_institution', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('user2', models.ForeignKey(related_name='user2_answer_institution', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AnswerStudent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer_score', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('answer_grade', models.CharField(max_length=30, null=True, blank=True)),
                ('double_entry', models.IntegerField(default=0, null=True, blank=True)),
                ('status', models.IntegerField(null=True, blank=True)),
                ('creation_date', models.DateField(auto_now_add=True, null=True)),
                ('last_modified_date', models.DateField(auto_now=True, null=True)),
                ('flexi_data', models.CharField(max_length=30, null=True, blank=True)),
                ('last_modified_by', models.ForeignKey(related_name='last_modified_answer_student', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('question', models.ForeignKey(to='schools.Question')),
                ('user1', models.ForeignKey(related_name='user1', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('user2', models.ForeignKey(related_name='user2', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='answer',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='last_modified_by',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='user1',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='user2',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.AlterUniqueTogether(
            name='answerstudent',
            unique_together=set([('question', 'flexi_data')]),
        ),
        migrations.AlterUniqueTogether(
            name='answerinstitution',
            unique_together=set([('question', 'flexi_data')]),
        ),
    ]
