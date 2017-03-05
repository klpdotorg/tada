# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0006_auto_20170303_2217'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='boundary',
            options={'ordering': ['name'], 'permissions': (('add_institution', 'Add Institution'), ('add_student', 'Add Student'), ('add_staff', 'Add Staff'), ('add_class', 'Add Class'))},
        ),
    ]
