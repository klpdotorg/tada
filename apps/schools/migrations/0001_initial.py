# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import schools.models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicYear',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20)),
                ('active', models.IntegerField(default=0, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AnswerInstitution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer_score', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('answer_grade', models.CharField(max_length=30, null=True, blank=True)),
                ('double_entry', models.IntegerField(default=0, null=True, blank=True)),
                ('status', models.IntegerField(null=True, blank=True)),
                ('creation_date', models.DateField(auto_now_add=True, null=True)),
                ('last_modified_date', models.DateField(auto_now=True, null=True)),
                ('flexi_data', models.CharField(max_length=30, null=True, blank=True)),
                ('last_modified_by', models.ForeignKey(related_name='last_modified_answer_institution', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AnswerStudent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer_score', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('answer_grade', models.CharField(max_length=30, null=True, blank=True)),
                ('double_entry', models.IntegerField(default=0, null=True, blank=True)),
                ('status', models.IntegerField(null=True, blank=True)),
                ('creation_date', models.DateField(auto_now_add=True, null=True)),
                ('last_modified_date', models.DateField(auto_now=True, null=True)),
                ('flexi_data', models.CharField(max_length=30, null=True, blank=True)),
                ('last_modified_by', models.ForeignKey(related_name='last_modified_answer_student', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Assessment_Institution_Association',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.IntegerField(default=2, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Assessment_StudentGroup_Association',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.IntegerField(default=2, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AssessmentInstitution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('start_date', models.DateField(default=datetime.date.today, max_length=20)),
                ('end_date', models.DateField(default=schools.models.default_end_date, max_length=20)),
                ('query', models.CharField(max_length=500, null=True, blank=True)),
                ('active', models.IntegerField(default=2, null=True, blank=True)),
                ('double_entry', models.BooleanField(default=True, verbose_name=b'Requires double entry')),
                ('flexi_assessment', models.BooleanField(default=False, verbose_name=b'Allows multiple sets of answer per assessment')),
                ('primary_field_name', models.CharField(max_length=500, null=True, blank=True)),
                ('primary_field_type', models.IntegerField(default=3, null=True, choices=[(0, b'Default'), (1, b'Integer'), (2, b'Char'), (3, b'Date'), (4, b'Lookup')])),
            ],
            options={
                'ordering': ['start_date'],
            },
        ),
        migrations.CreateModel(
            name='AssessmentStudent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('start_date', models.DateField(default=datetime.date.today, max_length=20)),
                ('end_date', models.DateField(default=schools.models.default_end_date, max_length=20)),
                ('query', models.CharField(max_length=500, null=True, blank=True)),
                ('active', models.IntegerField(default=2, null=True, blank=True)),
                ('double_entry', models.BooleanField(default=True, verbose_name=b'Requires double entry')),
                ('flexi_assessment', models.BooleanField(default=False, verbose_name=b'Allows multiple sets of answer per assessment')),
                ('primary_field_name', models.CharField(max_length=500, null=True, blank=True)),
                ('primary_field_type', models.IntegerField(default=3, null=True, choices=[(0, b'Default'), (1, b'Integer'), (2, b'Char'), (3, b'Date'), (4, b'Lookup')])),
            ],
            options={
                'ordering': ['start_date'],
            },
        ),
        migrations.CreateModel(
            name='Boundary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('active', models.IntegerField(default=2, null=True, blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Boundary_Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('boundary_category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Boundary_Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('boundary_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50, null=True, blank=True)),
                ('last_name', models.CharField(max_length=50, null=True, blank=True)),
                ('uid', models.CharField(max_length=100, null=True, blank=True)),
                ('dob', models.DateField(max_length=20)),
                ('gender', models.CharField(default=b'male', max_length=10, choices=[(b'male', b'male'), (b'female', b'female')])),
            ],
            options={
                'ordering': ['first_name', 'middle_name', 'last_name'],
            },
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dise_code', models.CharField(max_length=14, null=True, blank=True)),
                ('name', models.CharField(max_length=300)),
                ('institution_gender', models.CharField(default=b'co-ed', max_length=10, choices=[(b'boys', b'boys'), (b'girls', b'girls'), (b'co-ed', b'co-ed')])),
                ('active', models.IntegerField(default=2, null=True, blank=True)),
                ('boundary', models.ForeignKey(to='schools.Boundary')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Institution_address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=1000)),
                ('area', models.CharField(max_length=200, null=True, blank=True)),
                ('pincode', models.CharField(max_length=100, null=True, blank=True)),
                ('landmark', models.CharField(help_text=b'Can be comma separated', max_length=1000, null=True, blank=True)),
                ('instidentification', models.CharField(help_text=b'Can be comma separated', max_length=1000, null=True, blank=True)),
                ('instidentification2', models.CharField(help_text=b'Can be comma separated', max_length=1000, null=True, blank=True)),
                ('route_information', models.CharField(help_text=b'Can be comma separated', max_length=500, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Institution_Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('category_type', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Institution_Management',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Moi_Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProgrammeInstitution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500, null=True, blank=True)),
                ('start_date', models.DateField(default=datetime.date.today, max_length=20)),
                ('end_date', models.DateField(default=schools.models.default_end_date, max_length=20)),
                ('active', models.IntegerField(default=2, null=True, blank=True)),
                ('programme_institution_category', models.ForeignKey(blank=True, to='schools.Boundary_Type', null=True)),
            ],
            options={
                'ordering': ['-start_date', '-end_date', 'name'],
            },
        ),
        migrations.CreateModel(
            name='ProgrammeStudent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500, null=True, blank=True)),
                ('start_date', models.DateField(default=datetime.date.today, max_length=20)),
                ('end_date', models.DateField(default=schools.models.default_end_date, max_length=20)),
                ('active', models.IntegerField(default=2, null=True, blank=True)),
                ('programme_institution_category', models.ForeignKey(blank=True, to='schools.Boundary_Type', null=True)),
            ],
            options={
                'ordering': ['-start_date', '-end_date', 'name'],
            },
        ),
        migrations.CreateModel(
            name='QuestionInstitution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('question_type', models.IntegerField(default=1, choices=[(1, b'Marks'), (2, b'Grade')])),
                ('score_min', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('score_max', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('grade', models.CharField(max_length=100, null=True, blank=True)),
                ('order', models.IntegerField()),
                ('double_entry', models.BooleanField(default=True)),
                ('active', models.IntegerField(default=2, null=True, blank=True)),
                ('assessment', models.ForeignKey(to='schools.AssessmentInstitution')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='QuestionStudent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('question_type', models.IntegerField(default=1, choices=[(1, b'Marks'), (2, b'Grade')])),
                ('score_min', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('score_max', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('grade', models.CharField(max_length=100, null=True, blank=True)),
                ('order', models.IntegerField()),
                ('double_entry', models.BooleanField(default=True)),
                ('active', models.IntegerField(default=2, null=True, blank=True)),
                ('assessment', models.ForeignKey(to='schools.AssessmentStudent')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Relations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relation_type', models.CharField(default=b'Mother', max_length=10, choices=[(b'Mother', b'Mother'), (b'Father', b'Father'), (b'Siblings', b'Siblings')])),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=50, null=True, blank=True)),
                ('last_name', models.CharField(max_length=50, null=True, blank=True)),
                ('child', models.ForeignKey(to='schools.Child')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50, null=True, blank=True)),
                ('last_name', models.CharField(max_length=50, null=True, blank=True)),
                ('uid', models.CharField(max_length=100, null=True, blank=True)),
                ('doj', models.DateField(max_length=20, null=True, blank=True)),
                ('gender', models.CharField(default=b'female', max_length=10, choices=[(b'male', b'male'), (b'female', b'female')])),
                ('active', models.IntegerField(default=2, null=True, blank=True)),
                ('institution', models.ForeignKey(blank=True, to='schools.Institution', null=True)),
                ('mt', models.ForeignKey(default=1, to='schools.Moi_Type')),
            ],
            options={
                'ordering': ['first_name', 'middle_name', 'last_name'],
            },
        ),
        migrations.CreateModel(
            name='Staff_Qualifications',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qualification', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Staff_StudentGroupRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.IntegerField(default=2, null=True, blank=True)),
                ('academic', models.ForeignKey(default=schools.models.current_academic, to='schools.AcademicYear')),
                ('staff', models.ForeignKey(to='schools.Staff')),
            ],
        ),
        migrations.CreateModel(
            name='Staff_Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('staff_type', models.CharField(max_length=100)),
                ('category_type', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('other_student_id', models.CharField(max_length=100, null=True, blank=True)),
                ('active', models.IntegerField(default=2, null=True, blank=True)),
                ('child', models.ForeignKey(to='schools.Child')),
            ],
            options={
                'ordering': ['child__first_name'],
            },
        ),
        migrations.CreateModel(
            name='Student_StudentGroupRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.IntegerField(default=2, null=True, blank=True)),
                ('academic', models.ForeignKey(default=schools.models.current_academic, to='schools.AcademicYear')),
                ('student', models.ForeignKey(to='schools.Student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('section', models.CharField(default=b'', max_length=10, blank=True, choices=[(b'', b'No Section'), (b'A', b'A'), (b'B', b'B'), (b'C', b'C'), (b'D', b'D'), (b'E', b'E'), (b'F', b'F'), (b'G', b'G'), (b'H', b'H'), (b'I', b'I'), (b'J', b'J'), (b'K', b'K'), (b'L', b'L'), (b'M', b'M'), (b'N', b'N'), (b'O', b'O'), (b'P', b'P'), (b'Q', b'Q'), (b'R', b'R'), (b'S', b'S'), (b'T', b'T'), (b'U', b'U'), (b'V', b'V'), (b'W', b'W'), (b'X', b'X'), (b'Y', b'Y'), (b'Z', b'Z')])),
                ('active', models.IntegerField(default=2, null=True, blank=True)),
                ('group_type', models.CharField(default=b'Class', max_length=10, choices=[(b'Class', b'Class'), (b'Center', b'Center')])),
                ('institution', models.ForeignKey(to='schools.Institution')),
            ],
            options={
                'ordering': ['name', 'section'],
            },
        ),
        migrations.AddField(
            model_name='student_studentgrouprelation',
            name='student_group',
            field=models.ForeignKey(to='schools.StudentGroup'),
        ),
        migrations.AddField(
            model_name='staff_studentgrouprelation',
            name='student_group',
            field=models.ForeignKey(to='schools.StudentGroup'),
        ),
        migrations.AddField(
            model_name='staff',
            name='qualification',
            field=models.ManyToManyField(to='schools.Staff_Qualifications', blank=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='staff_type',
            field=models.ForeignKey(default=1, to='schools.Staff_Type'),
        ),
        migrations.AddField(
            model_name='institution',
            name='cat',
            field=models.ForeignKey(blank=True, to='schools.Institution_Category', null=True),
        ),
        migrations.AddField(
            model_name='institution',
            name='inst_address',
            field=models.ForeignKey(blank=True, to='schools.Institution_address', null=True),
        ),
        migrations.AddField(
            model_name='institution',
            name='languages',
            field=models.ManyToManyField(to='schools.Moi_Type'),
        ),
        migrations.AddField(
            model_name='institution',
            name='mgmt',
            field=models.ForeignKey(default=b'1', to='schools.Institution_Management'),
        ),
        migrations.AddField(
            model_name='child',
            name='mt',
            field=models.ForeignKey(default=b'1', to='schools.Moi_Type'),
        ),
        migrations.AddField(
            model_name='boundary',
            name='boundary_category',
            field=models.ForeignKey(blank=True, to='schools.Boundary_Category', null=True),
        ),
        migrations.AddField(
            model_name='boundary',
            name='boundary_type',
            field=models.ForeignKey(blank=True, to='schools.Boundary_Type', null=True),
        ),
        migrations.AddField(
            model_name='boundary',
            name='parent',
            field=models.ForeignKey(blank=True, to='schools.Boundary', null=True),
        ),
        migrations.AddField(
            model_name='assessmentstudent',
            name='programme',
            field=models.ForeignKey(to='schools.ProgrammeStudent'),
        ),
        migrations.AddField(
            model_name='assessmentinstitution',
            name='programme',
            field=models.ForeignKey(to='schools.ProgrammeInstitution'),
        ),
        migrations.AddField(
            model_name='assessment_studentgroup_association',
            name='assessment',
            field=models.ForeignKey(to='schools.AssessmentStudent'),
        ),
        migrations.AddField(
            model_name='assessment_studentgroup_association',
            name='student_group',
            field=models.ForeignKey(to='schools.StudentGroup'),
        ),
        migrations.AddField(
            model_name='assessment_institution_association',
            name='assessment',
            field=models.ForeignKey(to='schools.AssessmentStudent'),
        ),
        migrations.AddField(
            model_name='assessment_institution_association',
            name='institution',
            field=models.ForeignKey(to='schools.Institution'),
        ),
        migrations.AddField(
            model_name='answerstudent',
            name='question',
            field=models.ForeignKey(to='schools.QuestionStudent'),
        ),
        migrations.AddField(
            model_name='answerstudent',
            name='user1',
            field=models.ForeignKey(related_name='user1', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='answerstudent',
            name='user2',
            field=models.ForeignKey(related_name='user2', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='answerinstitution',
            name='question',
            field=models.ForeignKey(to='schools.QuestionInstitution'),
        ),
        migrations.AddField(
            model_name='answerinstitution',
            name='user1',
            field=models.ForeignKey(related_name='user1_answer_institution', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='answerinstitution',
            name='user2',
            field=models.ForeignKey(related_name='user2_answer_institution', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='studentgroup',
            unique_together=set([('institution', 'name', 'section')]),
        ),
        migrations.AlterUniqueTogether(
            name='student_studentgrouprelation',
            unique_together=set([('student', 'student_group', 'academic')]),
        ),
        migrations.AlterUniqueTogether(
            name='staff_studentgrouprelation',
            unique_together=set([('staff', 'student_group', 'academic')]),
        ),
        migrations.AlterUniqueTogether(
            name='questionstudent',
            unique_together=set([('assessment', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='questioninstitution',
            unique_together=set([('assessment', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='assessmentstudent',
            unique_together=set([('programme', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='assessmentinstitution',
            unique_together=set([('programme', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='assessment_studentgroup_association',
            unique_together=set([('assessment', 'student_group')]),
        ),
        migrations.AlterUniqueTogether(
            name='assessment_institution_association',
            unique_together=set([('assessment', 'institution')]),
        ),
        migrations.AlterUniqueTogether(
            name='answerstudent',
            unique_together=set([('question', 'flexi_data')]),
        ),
        migrations.AlterUniqueTogether(
            name='answerinstitution',
            unique_together=set([('question', 'flexi_data')]),
        ),
    ]
