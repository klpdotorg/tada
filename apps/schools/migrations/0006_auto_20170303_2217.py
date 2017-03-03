# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0005_auto_20170302_1547'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='boundary',
            options={'ordering': ['name'], 'permissions': (('add_school', 'Add School'), ('add_student', 'Add Student'), ('add_staff', 'Add Staff'), ('add_class', 'Add Class'))},
        ),
    ]
