# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0009_auto_20150623_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relations',
            name='student',
            field=models.ForeignKey(related_name='relations', to='schools.Student'),
        ),
    ]
