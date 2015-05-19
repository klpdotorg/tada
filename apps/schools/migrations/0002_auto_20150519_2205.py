# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='academicyear',
            name='end_year',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AddField(
            model_name='academicyear',
            name='start_year',
            field=models.IntegerField(default=0, blank=True),
        ),
    ]
