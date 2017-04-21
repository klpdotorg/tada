# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0007_auto_20170321_0937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answerinstitution',
            name='flexi_data',
        ),
        migrations.RemoveField(
            model_name='answerstudent',
            name='flexi_data',
        ),
        migrations.RemoveField(
            model_name='answerstudentgroup',
            name='flexi_data',
        ),
        migrations.RemoveField(
            model_name='assessment',
            name='query',
        ),
        migrations.AlterField(
            model_name='answerinstitution',
            name='active',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='answerstudent',
            name='active',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='answerstudentgroup',
            name='active',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='active',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='assessmentinstitutionassociation',
            name='active',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='assessmentstudentgroupassociation',
            name='active',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='programme',
            name='active',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='programme',
            name='programme_institution_category',
            field=models.ForeignKey(to='schools.BoundaryType'),
        ),
        migrations.AlterField(
            model_name='question',
            name='active',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='staffstudentgrouprelation',
            name='active',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='student',
            name='active',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(default='one-off-value', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studentgroup',
            name='active',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='studentstudentgrouprelation',
            name='active',
            field=models.IntegerField(default=2),
        ),
    ]
