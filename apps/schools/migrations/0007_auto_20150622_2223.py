# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0006_auto_20150528_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionstudent',
            name='order',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
