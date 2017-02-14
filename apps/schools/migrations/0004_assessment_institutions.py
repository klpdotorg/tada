# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0003_auto_20161122_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessment',
            name='institutions',
            field=models.ManyToManyField(to='schools.Institution', null=True, through='schools.AssessmentInstitutionAssociation', blank=True),
        ),
    ]
