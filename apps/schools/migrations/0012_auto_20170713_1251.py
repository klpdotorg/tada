# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0011_assessment_studentgroups'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50, null=True, blank=True)),
                ('last_name', models.CharField(max_length=50, null=True, blank=True)),
                ('gender', models.CharField(default=b'male', max_length=10, choices=[(b'male', b'male'), (b'female', b'female')])),
                ('qualification', models.CharField(max_length=100, null=True, blank=True)),
                ('total_work_experience_years', models.IntegerField(default=0, null=True, blank=True)),
                ('total_work_experience_months', models.IntegerField(default=0, null=True, blank=True)),
                ('subject', models.CharField(max_length=100, null=True, blank=True)),
                ('contact_no', models.CharField(max_length=20, null=True, blank=True)),
                ('address', models.CharField(max_length=1000, null=True, blank=True)),
                ('area', models.CharField(max_length=200, null=True, blank=True)),
                ('pincode', models.CharField(max_length=100, null=True, blank=True)),
                ('active', models.IntegerField(default=2)),
                ('institution', models.ForeignKey(to='schools.Institution')),
            ],
        ),
        migrations.AlterField(
            model_name='programme',
            name='programme_institution_category',
            field=models.ForeignKey(default=1, to='schools.BoundaryType'),
        ),
    ]
