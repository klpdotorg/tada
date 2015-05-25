# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import schools.models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0003_auto_20150521_1211'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssessmentInstitutionAssociation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.IntegerField(default=2, null=True, blank=True)),
                ('assessment', models.ForeignKey(to='schools.AssessmentStudent')),
                ('institution', models.ForeignKey(to='schools.Institution')),
            ],
        ),
        migrations.CreateModel(
            name='AssessmentStudentGroupAssociation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.IntegerField(default=2, null=True, blank=True)),
                ('assessment', models.ForeignKey(to='schools.AssessmentStudent')),
                ('student_group', models.ForeignKey(to='schools.StudentGroup')),
            ],
        ),
        migrations.CreateModel(
            name='StaffStudentGroupRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.IntegerField(default=2, null=True, blank=True)),
                ('academic', models.ForeignKey(default=schools.models.current_academic, to='schools.AcademicYear')),
                ('staff', models.ForeignKey(to='schools.Staff')),
                ('student_group', models.ForeignKey(to='schools.StudentGroup')),
            ],
        ),
        migrations.CreateModel(
            name='StudentStudentGroupRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.IntegerField(default=2, null=True, blank=True)),
                ('academic', models.ForeignKey(default=schools.models.current_academic, to='schools.AcademicYear')),
                ('student', models.ForeignKey(to='schools.Student')),
                ('student_group', models.ForeignKey(to='schools.StudentGroup')),
            ],
        ),
        migrations.RenameModel(
            old_name='Boundary_Category',
            new_name='BoundaryCategory',
        ),
        migrations.RenameModel(
            old_name='Boundary_Type',
            new_name='BoundaryType',
        ),
        migrations.RenameModel(
            old_name='Institution_Category',
            new_name='InstitutionCategory',
        ),
        migrations.RenameModel(
            old_name='Institution_Management',
            new_name='InstitutionManagement',
        ),
        migrations.RenameModel(
            old_name='Moi_Type',
            new_name='MoiType',
        ),
        migrations.RenameModel(
            old_name='Staff_Qualifications',
            new_name='StaffQualifications',
        ),
        migrations.RenameModel(
            old_name='Staff_Type',
            new_name='StaffType',
        ),
        migrations.AlterUniqueTogether(
            name='assessment_institution_association',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='assessment_institution_association',
            name='assessment',
        ),
        migrations.RemoveField(
            model_name='assessment_institution_association',
            name='institution',
        ),
        migrations.AlterUniqueTogether(
            name='assessment_studentgroup_association',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='assessment_studentgroup_association',
            name='assessment',
        ),
        migrations.RemoveField(
            model_name='assessment_studentgroup_association',
            name='student_group',
        ),
        migrations.AlterUniqueTogether(
            name='staff_studentgrouprelation',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='staff_studentgrouprelation',
            name='academic',
        ),
        migrations.RemoveField(
            model_name='staff_studentgrouprelation',
            name='staff',
        ),
        migrations.RemoveField(
            model_name='staff_studentgrouprelation',
            name='student_group',
        ),
        migrations.AlterUniqueTogether(
            name='student_studentgrouprelation',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='student_studentgrouprelation',
            name='academic',
        ),
        migrations.RemoveField(
            model_name='student_studentgrouprelation',
            name='student',
        ),
        migrations.RemoveField(
            model_name='student_studentgrouprelation',
            name='student_group',
        ),
        migrations.DeleteModel(
            name='Assessment_Institution_Association',
        ),
        migrations.DeleteModel(
            name='Assessment_StudentGroup_Association',
        ),
        migrations.DeleteModel(
            name='Staff_StudentGroupRelation',
        ),
        migrations.DeleteModel(
            name='Student_StudentGroupRelation',
        ),
        migrations.AlterUniqueTogether(
            name='studentstudentgrouprelation',
            unique_together=set([('student', 'student_group', 'academic')]),
        ),
        migrations.AlterUniqueTogether(
            name='staffstudentgrouprelation',
            unique_together=set([('staff', 'student_group', 'academic')]),
        ),
        migrations.AlterUniqueTogether(
            name='assessmentstudentgroupassociation',
            unique_together=set([('assessment', 'student_group')]),
        ),
        migrations.AlterUniqueTogether(
            name='assessmentinstitutionassociation',
            unique_together=set([('assessment', 'institution')]),
        ),
    ]
