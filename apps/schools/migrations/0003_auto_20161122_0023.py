# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0002_studentgroup_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentgroup',
            name='students',
            field=models.ManyToManyField(related_name='studentgroups', through='schools.StudentStudentGroupRelation', to='schools.Student'),
        ),
    ]
