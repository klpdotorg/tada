# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0008_auto_20150623_1020'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='answerstudent',
            unique_together=set([]),
        ),
    ]
