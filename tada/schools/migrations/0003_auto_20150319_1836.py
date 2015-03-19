# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import schools.models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0002_auto_20150319_1725'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssessmentInstitution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('start_date', models.DateField(default=datetime.date.today, max_length=20)),
                ('end_date', models.DateField(default=schools.models.default_end_date, max_length=20)),
                ('query', models.CharField(max_length=500, null=True, blank=True)),
                ('active', models.IntegerField(default=2, null=True, blank=True)),
                ('double_entry', models.BooleanField(default=True, verbose_name=b'Requires double entry')),
                ('flexi_assessment', models.BooleanField(default=False, verbose_name=b'Allows multiple sets of answer per assessment')),
                ('primary_field_name', models.CharField(max_length=500, null=True, blank=True)),
                ('primary_field_type', models.IntegerField(default=3, null=True, choices=[(0, b'Default'), (1, b'Integer'), (2, b'Char'), (3, b'Date'), (4, b'Lookup')])),
                ('programme', models.ForeignKey(to='schools.Programme')),
            ],
            options={
                'ordering': ['start_date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AssessmentStudent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('start_date', models.DateField(default=datetime.date.today, max_length=20)),
                ('end_date', models.DateField(default=schools.models.default_end_date, max_length=20)),
                ('query', models.CharField(max_length=500, null=True, blank=True)),
                ('active', models.IntegerField(default=2, null=True, blank=True)),
                ('double_entry', models.BooleanField(default=True, verbose_name=b'Requires double entry')),
                ('flexi_assessment', models.BooleanField(default=False, verbose_name=b'Allows multiple sets of answer per assessment')),
                ('primary_field_name', models.CharField(max_length=500, null=True, blank=True)),
                ('primary_field_type', models.IntegerField(default=3, null=True, choices=[(0, b'Default'), (1, b'Integer'), (2, b'Char'), (3, b'Date'), (4, b'Lookup')])),
                ('programme', models.ForeignKey(to='schools.Programme')),
            ],
            options={
                'ordering': ['start_date'],
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='assessment',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='assessment',
            name='programme',
        ),
        migrations.AlterUniqueTogether(
            name='assessment_class_association',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='assessment_class_association',
            name='assessment',
        ),
        migrations.RemoveField(
            model_name='assessment_class_association',
            name='student_group',
        ),
        migrations.DeleteModel(
            name='Assessment_Class_Association',
        ),
        migrations.AlterUniqueTogether(
            name='assessment_lookup',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='assessment_lookup',
            name='assessment',
        ),
        migrations.DeleteModel(
            name='Assessment_Lookup',
        ),
        migrations.AlterUniqueTogether(
            name='userassessmentpermissions',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='userassessmentpermissions',
            name='assessment',
        ),
        migrations.RemoveField(
            model_name='userassessmentpermissions',
            name='instituion',
        ),
        migrations.RemoveField(
            model_name='userassessmentpermissions',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserAssessmentPermissions',
        ),
        migrations.AlterUniqueTogether(
            name='assessmentstudent',
            unique_together=set([('programme', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='assessmentinstitution',
            unique_together=set([('programme', 'name')]),
        ),
        migrations.AlterField(
            model_name='assessment_institution_association',
            name='assessment',
            field=models.ForeignKey(to='schools.AssessmentStudent'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='assessment_studentgroup_association',
            name='assessment',
            field=models.ForeignKey(to='schools.AssessmentStudent'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='assessment',
            field=models.ForeignKey(to='schools.AssessmentStudent'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Assessment',
        ),
    ]
