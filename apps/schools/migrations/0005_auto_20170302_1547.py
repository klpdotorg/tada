# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0004_assessment_institutions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boundarycategory',
            old_name='boundary_category',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='boundarytype',
            old_name='boundary_type',
            new_name='name',
        ),
    ]
