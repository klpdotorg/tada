# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0002_auto_20150519_2205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='child',
            name='mt',
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['first_name', 'middle_name', 'last_name']},
        ),
        migrations.RemoveField(
            model_name='institution',
            name='inst_address',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='student',
            name='child',
        ),
        migrations.RemoveField(
            model_name='student',
            name='other_student_id',
        ),
        migrations.AddField(
            model_name='institution',
            name='address',
            field=models.CharField(default=b'NA', max_length=1000),
        ),
        migrations.AddField(
            model_name='institution',
            name='area',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='institution',
            name='instidentification',
            field=models.CharField(help_text=b'Can be comma separated', max_length=1000, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='institution',
            name='instidentification2',
            field=models.CharField(help_text=b'Can be comma separated', max_length=1000, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='institution',
            name='landmark',
            field=models.CharField(help_text=b'Can be comma separated', max_length=1000, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='institution',
            name='pincode',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='institution',
            name='route_information',
            field=models.CharField(help_text=b'Can be comma separated', max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='dob',
            field=models.DateField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(default=b'male', max_length=10, choices=[(b'male', b'male'), (b'female', b'female')]),
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='middle_name',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='mt',
            field=models.ForeignKey(default=b'1', to='schools.Moi_Type'),
        ),
        migrations.AddField(
            model_name='student',
            name='uid',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='relations',
            name='child',
            field=models.ForeignKey(to='schools.Student'),
        ),
        migrations.DeleteModel(
            name='Child',
        ),
        migrations.DeleteModel(
            name='Institution_address',
        ),
    ]
