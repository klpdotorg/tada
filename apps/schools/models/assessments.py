#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
import datetime
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User
from .programs import ProgrammeInstitution, ProgrammeStudent
from .students import StudentGroup
from .institution import Institution, current_academic, default_end_date

PRIMARY_FIELD_TYPE = [(0, 'Default'),(1, 'Integer'), (2, 'Char'), (3, 'Date'), (4,
                      'Lookup')]
QUESTION_TYPE = [(1, 'Marks'), (2, 'Grade')]


ASSESSMENT_TYPE = [(1, 'Institution'), (2, 'Student Group'), (3,
                   'Student')]

class AssessmentInstitution(models.Model):
    """ This class stores information about Assessment """

    programme = models.ForeignKey(ProgrammeInstitution)
    name = models.CharField(max_length=100)
    start_date = models.DateField(max_length=20,
                                 default=datetime.date.today)
    end_date = models.DateField(max_length=20, default=default_end_date)
    query = models.CharField(max_length=500, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True, default=2)
    double_entry = models.BooleanField('Requires double entry',
            default=True)
    flexi_assessment = \
        models.BooleanField('Allows multiple sets of answer per assessment'
                            , default=False)
    primary_field_name = models.CharField(max_length=500, blank=True,
            null=True)
    PRIMARY_FIELD_TYPE = \
        models.IntegerField(choices=PRIMARY_FIELD_TYPE, default=3,
                            null=True)

    class Meta:
        unique_together = (('programme', 'name'), )
        ordering = ['start_date']

    def __unicode__(self):
        return '%s' % self.name

    def get_view_url(self):
        return '/assessment/%s/view/' % self.id

    def get_edit_url(self):
        return '/assessment/%s/update/' % self.id

    def getChild(self):
        if Question.objects.filter(assessment__id=self.id,
                                   active=2).count():
            return True
        else:
            return False

    def getModuleName(self):
        return 'assessmentInstitution'

class AssessmentStudent(models.Model):
    """ This class stores information about Assessment """

    programme = models.ForeignKey(ProgrammeStudent)
    name = models.CharField(max_length=100)
    start_date = models.DateField(max_length=20,
                                 default=datetime.date.today)
    end_date = models.DateField(max_length=20, default=default_end_date)
    query = models.CharField(max_length=500, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True, default=2)
    double_entry = models.BooleanField('Requires double entry',
            default=True)
    flexi_assessment = \
        models.BooleanField('Allows multiple sets of answer per assessment'
                            , default=False)
    primary_field_name = models.CharField(max_length=500, blank=True,
            null=True)
    PRIMARY_FIELD_TYPE = \
        models.IntegerField(choices=PRIMARY_FIELD_TYPE, default=3,
                            null=True)

    class Meta:

        unique_together = (('programme', 'name'), )
        ordering = ['start_date']

    def __unicode__(self):
        return '%s' % self.name

    def get_view_url(self):
        return '/assessment/%s/view/' % self.id

    def get_edit_url(self):
        return '/assessment/%s/update/' % self.id

    def getChild(self):
        if Question.objects.filter(assessment__id=self.id,
                                   active=2).count():
            return True
        else:
            return False

    def getModuleName(self):
        return 'assessmentStudent'

class AssessmentStudentGroupAssociation(models.Model):
    '''This Class stores the Assessment and Student Group Association Information'''

    assessment = models.ForeignKey(AssessmentStudent)
    student_group = models.ForeignKey(StudentGroup)
    active = models.IntegerField(blank=True, null=True, default=2)


    def save(self, *args, **kwargs):
        # custom save method
        #pdb.set_trace()
        from django.db import connection
        connection.features.can_return_id_from_insert = False
        #print "save"

        #print "Access", self.active
        self.full_clean()
        super(Assessment_StudentGroup_Association, self).save(*args, **kwargs)

    class Meta:

        unique_together = (('assessment', 'student_group'), )

class AssessmentInstitutionAssociation(models.Model):
    '''This Class stores the Assessment and Student Group Association Information'''

    assessment = models.ForeignKey(AssessmentStudent)
    institution = models.ForeignKey(Institution)
    active = models.IntegerField(blank=True, null=True, default=2)

    class Meta:

        unique_together = (('assessment', 'institution'), )


class QuestionStudent(models.Model):
    """ This class stores Assessment detail information """

    assessment = models.ForeignKey(AssessmentStudent)
    name = models.CharField(max_length=200)
    question_type = models.IntegerField(choices=QUESTION_TYPE, default=1)
    score_min = models.DecimalField(max_digits=10, decimal_places=2,
                                   blank=True, null=True)
    score_max = models.DecimalField(max_digits=10, decimal_places=2,
                                   blank=True, null=True)
    grade = models.CharField(max_length=100, blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    double_entry = models.BooleanField(default=True)
    active = models.IntegerField(blank=True, null=True, default=2)

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
        return 'questionStudent'

    def get_view_url(self):
        return '/question/%s/view/' % self.id

    def get_edit_url(self):
        return '/question/%s/update/' % self.id


class QuestionInstitution(models.Model):
    """ This class stores Assessment detail information """

    assessment = models.ForeignKey(AssessmentInstitution)
    name = models.CharField(max_length=200)
    question_type = models.IntegerField(choices=QUESTION_TYPE, default=1)
    score_min = models.DecimalField(max_digits=10, decimal_places=2,
                                   blank=True, null=True)
    score_max = models.DecimalField(max_digits=10, decimal_places=2,
                                   blank=True, null=True)
    grade = models.CharField(max_length=100, blank=True, null=True)
    order = models.IntegerField()
    double_entry = models.BooleanField(default=True)
    active = models.IntegerField(blank=True, null=True, default=2)

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
        return 'questionInstitution'

    def get_view_url(self):
        return '/question/%s/view/' % self.id

    def get_edit_url(self):
        return '/question/%s/update/' % self.id



class AnswerStudent(models.Model):
    """ This class stores information about student marks and grade """
    
    question = models.ForeignKey(QuestionStudent)

    # student = models.IntegerField(blank = True, null = True,default=0) # models.ForeignKey(Student)

    answer_score = models.DecimalField(max_digits=10, decimal_places=2,
            blank=True, null=True)
    answer_grade = models.CharField(max_length=30, blank=True, null=True)
    double_entry = models.IntegerField(blank=True, null=True, default=0)
    status = models.IntegerField(blank=True, null=True)
    user1 = models.ForeignKey(User, blank=True, null=True,
                              related_name='user1')
    user2 = models.ForeignKey(User, blank=True, null=True,
                              related_name='user2')
    creation_date = models.DateField(auto_now_add=True,
                                    blank=True, null=True)
    last_modified_date = models.DateField(auto_now=True,
            blank=True, null=True)
    last_modified_by = models.ForeignKey(User, blank=True, null=True,
            related_name='last_modified_answer_student')
    flexi_data = models.CharField(max_length=30, blank=True, null=True)
    student_id = models.PositiveIntegerField(default=0)
    active = models.IntegerField(blank=True, null=True, default=2)

    def save(self, *args, **kwargs):
        # custom save method
        #pdb.set_trace()
        from django.db import connection
        connection.features.can_return_id_from_insert = False
        #print "save"

        #print "=================== status is", self.status
        self.full_clean()
        super(AnswerStudent, self).save(*args, **kwargs)


class AnswerStudentTemp(models.Model):
    """ This Temp table class stores information about student marks and grade before double entry"""
    
    question = models.ForeignKey(QuestionStudent)

    # student = models.IntegerField(blank = True, null = True,default=0) # models.ForeignKey(Student)

    answer_score = models.DecimalField(max_digits=10, decimal_places=2,
            blank=True, null=True)
    answer_grade = models.CharField(max_length=30, blank=True, null=True)
    double_entry = models.IntegerField(blank=True, null=True, default=0)
    status = models.IntegerField(blank=True, null=True)
    user1 = models.ForeignKey(User, blank=True, null=True,
                              related_name='temp_user1')
    user2 = models.ForeignKey(User, blank=True, null=True,
                              related_name='temp_user2')
    creation_date = models.DateField(auto_now_add=True,
                                    blank=True, null=True)
    last_modified_date = models.DateField(auto_now=True,
            blank=True, null=True)
    last_modified_by = models.ForeignKey(User, blank=True, null=True,
            related_name='temp_last_modified_answer_student')
    flexi_data = models.CharField(max_length=30, blank=True, null=True)

    def save(self, *args, **kwargs):
        # custom save method
        #pdb.set_trace()
        from django.db import connection
        connection.features.can_return_id_from_insert = False
        #print "save"

        #print "=================== status is", self.status
        self.full_clean()
        super(AnswerStudentTemp, self).save(*args, **kwargs)


class AnswerInstitution(models.Model):
    """ This class stores information about student marks and grade """
    
    question = models.ForeignKey(QuestionInstitution)

    # student = models.IntegerField(blank = True, null = True,default=0) # models.ForeignKey(Student)

    answer_score = models.DecimalField(max_digits=10, decimal_places=2,
            blank=True, null=True)
    answer_grade = models.CharField(max_length=30, blank=True, null=True)
    double_entry = models.IntegerField(blank=True, null=True, default=0)
    status = models.IntegerField(blank=True, null=True)
    user1 = models.ForeignKey(User, blank=True, null=True,
                              related_name='user1_answer_institution')
    user2 = models.ForeignKey(User, blank=True, null=True,
                              related_name='user2_answer_institution')
    creation_date = models.DateField(auto_now_add=True,
                                    blank=True, null=True)
    last_modified_date = models.DateField(auto_now=True,
            blank=True, null=True)
    last_modified_by = models.ForeignKey(User, blank=True, null=True,
            related_name='last_modified_answer_institution')
    flexi_data = models.CharField(max_length=30, blank=True, null=True)
    institution_id = models.PositiveIntegerField(default=0)
    active = models.IntegerField(blank=True, null=True, default=2)

    def save(self, *args, **kwargs):
        # custom save method
        #pdb.set_trace()
        from django.db import connection
        connection.features.can_return_id_from_insert = False
        #print "save"

        #print "=================== status is", self.status
        self.full_clean()
        super(AnswerInstitution, self).save(*args, **kwargs)
