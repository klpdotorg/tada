# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schools', '0006_auto_20170309_2011'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerStudentGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer_score', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('answer_grade', models.CharField(max_length=30, null=True, blank=True)),
                ('double_entry', models.IntegerField(default=0, null=True, blank=True)),
                ('status', models.IntegerField(null=True, blank=True)),
                ('creation_date', models.DateField(auto_now_add=True, null=True)),
                ('last_modified_date', models.DateField(auto_now=True, null=True)),
                ('flexi_data', models.CharField(max_length=30, null=True, blank=True)),
                ('active', models.IntegerField(default=2, null=True, blank=True)),
                ('last_modified_by', models.ForeignKey(related_name='last_modified_answer_studentgroup', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['question'],
            },
        ),
        migrations.AddField(
            model_name='question',
            name='desc',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='answerinstitution',
            unique_together=set([('question', 'institution')]),
        ),
        migrations.AlterUniqueTogether(
            name='relations',
            unique_together=set([('relation_type', 'student')]),
        ),
        migrations.AddField(
            model_name='answerstudentgroup',
            name='question',
            field=models.ForeignKey(to='schools.Question'),
        ),
        migrations.AddField(
            model_name='answerstudentgroup',
            name='studentgroup',
            field=models.ForeignKey(to='schools.StudentGroup'),
        ),
        migrations.AddField(
            model_name='answerstudentgroup',
            name='user1',
            field=models.ForeignKey(related_name='ans_sg_user1', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='answerstudentgroup',
            name='user2',
            field=models.ForeignKey(related_name='ans_sg_user2', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='answerstudentgroup',
            unique_together=set([('question', 'studentgroup')]),
        ),
    ]
