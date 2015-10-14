# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0007_auto_20150622_2223'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='answerinstitution',
            unique_together=set([]),
        ),
    ]
