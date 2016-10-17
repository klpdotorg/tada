# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0013_auto_20160921_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessmentinstitutionassociation',
            name='assessment',
            field=models.ForeignKey(to='schools.AssessmentInstitution'),
        ),
    ]
