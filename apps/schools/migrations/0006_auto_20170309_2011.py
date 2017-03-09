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
            options={'ordering': ['name'], 'permissions': (('add_institution', 'Add Institution'),)},
        ),
        migrations.AlterModelOptions(
            name='institution',
            options={'ordering': ['name'], 'permissions': (('crud_student_class_staff', 'CRUD Student Class and Staff'),)},
        ),
    ]
