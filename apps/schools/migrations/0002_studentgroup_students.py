# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentgroup',
            name='students',
            field=models.ManyToManyField(related_name='students', through='schools.StudentStudentGroupRelation', to='schools.Student'),
        ),
    ]
