# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0004_auto_20150525_1357'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StaffQualifications',
            new_name='QualificationList',
        ),
    ]
