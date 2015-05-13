# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0004_auto_20150427_1912'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionInstitution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('question_type', models.IntegerField(default=1, choices=[(1, b'Marks'), (2, b'Grade')])),
                ('score_min', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('score_max', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('grade', models.CharField(max_length=100, null=True, blank=True)),
                ('order', models.IntegerField()),
                ('double_entry', models.BooleanField(default=True)),
                ('active', models.IntegerField(default=2, null=True, blank=True)),
                ('assessment', models.ForeignKey(to='schools.AssessmentInstitution')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='QuestionStudent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('question_type', models.IntegerField(default=1, choices=[(1, b'Marks'), (2, b'Grade')])),
                ('score_min', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('score_max', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('grade', models.CharField(max_length=100, null=True, blank=True)),
                ('order', models.IntegerField()),
                ('double_entry', models.BooleanField(default=True)),
                ('active', models.IntegerField(default=2, null=True, blank=True)),
                ('assessment', models.ForeignKey(to='schools.AssessmentStudent')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='question',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='question',
            name='assessment',
        ),
        migrations.AlterField(
            model_name='answerinstitution',
            name='question',
            field=models.ForeignKey(to='schools.QuestionInstitution'),
        ),
        migrations.AlterField(
            model_name='answerstudent',
            name='question',
            field=models.ForeignKey(to='schools.QuestionStudent'),
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AlterUniqueTogether(
            name='questionstudent',
            unique_together=set([('assessment', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='questioninstitution',
            unique_together=set([('assessment', 'name')]),
        ),
    ]
