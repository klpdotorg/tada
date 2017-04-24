# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0009_auto_20170423_1826'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assessment',
            options={'permissions': (('crud_answers', 'CRUD Answers'),)},
        ),
    ]
