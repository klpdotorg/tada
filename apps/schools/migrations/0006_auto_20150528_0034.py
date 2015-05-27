# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0005_auto_20150525_1558'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assessmentinstitution',
            old_name='primary_field_type',
            new_name='PRIMARY_FIELD_TYPE',
        ),
        migrations.RenameField(
            model_name='assessmentstudent',
            old_name='primary_field_type',
            new_name='PRIMARY_FIELD_TYPE',
        ),
        migrations.RenameField(
            model_name='relations',
            old_name='child',
            new_name='student',
        ),
    ]
