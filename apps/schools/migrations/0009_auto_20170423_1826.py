# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0008_auto_20170421_1015'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CompensationAuditLog',
        ),
        migrations.AlterModelOptions(
            name='answerstudent',
            options={},
        ),
        migrations.AlterModelOptions(
            name='answerstudentgroup',
            options={},
        ),
        migrations.AlterModelOptions(
            name='staff',
            options={},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={},
        ),
        migrations.RemoveField(
            model_name='answerinstitution',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='answerinstitution',
            name='last_modified_by',
        ),
        migrations.RemoveField(
            model_name='answerinstitution',
            name='last_modified_date',
        ),
        migrations.RemoveField(
            model_name='answerinstitution',
            name='user1',
        ),
        migrations.RemoveField(
            model_name='answerinstitution',
            name='user2',
        ),
        migrations.RemoveField(
            model_name='answerstudent',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='answerstudent',
            name='last_modified_by',
        ),
        migrations.RemoveField(
            model_name='answerstudent',
            name='last_modified_date',
        ),
        migrations.RemoveField(
            model_name='answerstudent',
            name='user1',
        ),
        migrations.RemoveField(
            model_name='answerstudent',
            name='user2',
        ),
        migrations.RemoveField(
            model_name='answerstudentgroup',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='answerstudentgroup',
            name='last_modified_by',
        ),
        migrations.RemoveField(
            model_name='answerstudentgroup',
            name='last_modified_date',
        ),
        migrations.RemoveField(
            model_name='answerstudentgroup',
            name='user1',
        ),
        migrations.RemoveField(
            model_name='answerstudentgroup',
            name='user2',
        ),
    ]
