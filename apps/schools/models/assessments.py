#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
import datetime
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User
from .programs import Programme
from .students import StudentGroup,Student
from .institution import Institution, current_academic, default_end_date

PRIMARY_FIELD_TYPE = [(0, 'Default'),(1, 'Integer'), (2, 'Char'), (3, 'Date'), (4,
                      'Lookup')]
QUESTION_TYPE = [(1, 'Marks'), (2, 'Grade')]


ASSESSMENT_TYPE = [(1, 'Institution'), (2, 'Student Group'), (3,
                   'Student')]


class Assessment(models.Model):
    """ This class stores information about Assessment """

    programme = models.ForeignKey(Programme)
    name = models.CharField(max_length=100)
    type = models.IntegerField(choices=ASSESSMENT_TYPE, default=3)
    start_date = models.DateField(max_length=20,
                                 default=datetime.date.today)
    end_date = models.DateField(max_length=20, default=default_end_date)
    active = models.IntegerField(default=2)
    double_entry = models.BooleanField('Requires double entry',
            default=True)
    institutions = models.ManyToManyField(
        'Institution',
        through='AssessmentInstitutionAssociation',
        blank=True,
        null=True,
    )

    class Meta:
        unique_together = (('programme', 'name'), )
        permissions = (
            ('crud_answers', 'CRUD Answers'),
        )

    def __unicode__(self):
        return '%s' % self.name

    def get_view_url(self):
        return '/assessment/%s/view/' % self.id

    def get_edit_url(self):
        return '/assessment/%s/update/' % self.id

    def getChild(self):
        if Question.objects.filter(assessment__id=self.id, active=2).count():
            return True
        else:
            return False

    def getModuleName(self):
        return 'assessment'


class AssessmentStudentGroupAssociation(models.Model):
    '''This Class stores the Assessment and Student Group Association Information'''

    assessment = models.ForeignKey(Assessment)
    student_group = models.ForeignKey(StudentGroup)
    active = models.IntegerField(default=2)

    class Meta:
        unique_together = (('assessment', 'student_group'), )


class AssessmentInstitutionAssociation(models.Model):
    '''This Class stores the Assessment and Student Group Association Information'''

    assessment = models.ForeignKey(Assessment)
    institution = models.ForeignKey(Institution)
    active = models.IntegerField(default=2)

    class Meta:
        unique_together = (('assessment', 'institution'), )


class Question(models.Model):
    """ This class stores Question detail information """

    assessment = models.ForeignKey(Assessment)
    name = models.CharField(max_length=200)
    question_type = models.IntegerField(choices=QUESTION_TYPE, default=1)
    score_min = models.DecimalField(max_digits=10, decimal_places=2,
                                   blank=True, null=True)
    score_max = models.DecimalField(max_digits=10, decimal_places=2,
                                   blank=True, null=True)
    grade = models.CharField(max_length=100, blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    double_entry = models.BooleanField(default=True)
    active = models.IntegerField(default=2)
    desc = models.CharField(max_length=500, null=True)

    class Meta:
        unique_together = (('assessment', 'name'), )
        ordering = ['order']

    def __unicode__(self):
        return self.name

    def getAllGrades(self):
        return gradeList

    def getSelectedGrades(self):
        if self.grade:
            return self.grade.split(',')
        else:
            return ''

    def getChild(self):
        return False

    def getModuleName(self):
        return 'question'

    def get_view_url(self):
        return '/question/%s/view/' % self.id

    def get_edit_url(self):
        return '/question/%s/update/' % self.id


class AnswerStudent(models.Model):
    """ This class stores information about student marks and grade """

    question = models.ForeignKey(Question)
    student = models.ForeignKey(Student)

    answer_score = models.DecimalField(max_digits=10, decimal_places=2,
            blank=True, null=True)
    answer_grade = models.CharField(max_length=30, blank=True, null=True)
    double_entry = models.IntegerField(blank=True, null=True, default=0)
    status = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(default=2)

    class Meta:
        unique_together = (('question', 'student'), )


class AnswerInstitution(models.Model):
    """ This class stores information about student marks and grade """

    question = models.ForeignKey(Question)
    institution = models.ForeignKey(Institution)

    answer_score = models.DecimalField(max_digits=10, decimal_places=2,
            blank=True, null=True)
    answer_grade = models.CharField(max_length=30, blank=True, null=True)
    double_entry = models.IntegerField(blank=True, null=True, default=0)
    status = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(default=2)

    class Meta:
        unique_together = (('question', 'institution'), )


class AnswerStudentGroup(models.Model):
    """ This class stores information about studentgroups marks and grade """

    question = models.ForeignKey(Question)
    studentgroup = models.ForeignKey(StudentGroup)

    answer_score = models.DecimalField(max_digits=10, decimal_places=2,
            blank=True, null=True)
    answer_grade = models.CharField(max_length=30, blank=True, null=True)
    double_entry = models.IntegerField(blank=True, null=True, default=0)
    status = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(default=2)

    class Meta:
        unique_together = (('question', 'studentgroup'), )
