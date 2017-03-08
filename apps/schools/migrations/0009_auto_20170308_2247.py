# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0008_auto_20170307_2230'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='boundary',
            options={'ordering': ['name'], 'permissions': (('add_institution', 'Add Institution'),)},
        ),
        migrations.AlterModelOptions(
            name='institution',
            options={'ordering': ['name'], 'permissions': (('add_student', 'Add Student'), ('add_staff', 'Add Staff'), ('add_studentgroup', 'Add StudentGroup'))},
        ),
    ]
