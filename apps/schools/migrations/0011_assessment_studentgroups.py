# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0010_auto_20170424_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessment',
            name='studentgroups',
            field=models.ManyToManyField(to='schools.StudentGroup', null=True, through='schools.AssessmentStudentGroupAssociation', blank=True),
        ),
    ]
