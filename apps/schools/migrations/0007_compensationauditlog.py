# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0006_auto_20150528_0034'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompensationAuditLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=100)),
                ('audit_time', models.DateField(default=datetime.date.today, max_length=20)),
                ('entity_name', models.CharField(max_length=100)),
                ('operation_type', models.CharField(max_length=20)),
                ('operation_value', models.CharField(max_length=20)),
            ],
        ),
    ]
