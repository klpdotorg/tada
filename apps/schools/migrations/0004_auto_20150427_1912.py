# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import schools.models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0003_auto_20150319_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgrammeInstitution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500, null=True, blank=True)),
                ('start_date', models.DateField(default=datetime.date.today, max_length=20)),
                ('end_date', models.DateField(default=schools.models.default_end_date, max_length=20)),
                ('active', models.IntegerField(default=2, null=True, blank=True)),
                ('programme_institution_category', models.ForeignKey(blank=True, to='schools.Boundary_Type', null=True)),
            ],
            options={
                'ordering': ['-start_date', '-end_date', 'name'],
            },
        ),
        migrations.CreateModel(
            name='ProgrammeStudent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500, null=True, blank=True)),
                ('start_date', models.DateField(default=datetime.date.today, max_length=20)),
                ('end_date', models.DateField(default=schools.models.default_end_date, max_length=20)),
                ('active', models.IntegerField(default=2, null=True, blank=True)),
                ('programme_institution_category', models.ForeignKey(blank=True, to='schools.Boundary_Type', null=True)),
            ],
            options={
                'ordering': ['-start_date', '-end_date', 'name'],
            },
        ),
        migrations.RemoveField(
            model_name='programme',
            name='programme_institution_category',
        ),
        migrations.RemoveField(
            model_name='taggeditem',
            name='content_type',
        ),
        migrations.AlterField(
            model_name='assessmentinstitution',
            name='programme',
            field=models.ForeignKey(to='schools.ProgrammeInstitution'),
        ),
        migrations.AlterField(
            model_name='assessmentstudent',
            name='programme',
            field=models.ForeignKey(to='schools.ProgrammeStudent'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='qualification',
            field=models.ManyToManyField(to='schools.Staff_Qualifications', blank=True),
        ),
        migrations.DeleteModel(
            name='Programme',
        ),
        migrations.DeleteModel(
            name='TaggedItem',
        ),
    ]
