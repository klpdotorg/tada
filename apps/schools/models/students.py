#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
import datetime
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from .institution import Institution,MoiType, AcademicYear,current_academic, default_end_date,Staff

GROUP_TYPE = [('Class', 'Class'), ('Center', 'Center')]
GENDER = [('male', 'male'), ('female', 'female')]
RELATION_TYPE = [('Mother', 'Mother'), ('Father', 'Father'), ('Siblings'
                 , 'Siblings')]
Alpha_list = [('', 'No Section')]
for typ in range(ord('a'), ord('z') + 1):
    alph = chr(typ).upper()
    typs = (alph, alph)
    Alpha_list.append(typs)

class Relations(models.Model):
    ''' This class stores relation information of the childrens'''

    relation_type = models.CharField(max_length=10,
            choices=RELATION_TYPE, default='Mother')
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    student = models.ForeignKey("Student", related_name="relations")

    def __unicode__(self):
        return '%s' % self.first_name

    def get_view_url(self):
        return ''


class StudentGroup(models.Model):
    ''' Here it holds the informaion of the class and section of the Institutions'''

    institution = models.ForeignKey(Institution)
    name = models.CharField(max_length=50)
    section = models.CharField(max_length=10, choices=Alpha_list,
                               blank=True, default='')
    active = models.IntegerField(blank=True, null=True, default=2)
    group_type = models.CharField(max_length=10, choices=GROUP_TYPE,
                                  default='Class')

    class Meta:

        unique_together = (('institution', 'name', 'section'), )
        ordering = ['name', 'section']

    def __unicode__(self):
        return '%s' % self.name

    def getChild(self):
        return False

    def getSchoolIdentity(self):
        return '%s: %s' % (self.institution__id, self.institution__name)

    def getModuleName(self):
        return 'studentgroup'

    def get_update_url(self):
        return '/studentgroup/%d/update/' % self.id

    def get_view_url(self):
        return '/studentgroup/%s/view/' % self.id

    def save(self, *args, **kwargs):
        # custom save method
        #pdb.set_trace()
        from django.db import connection
        connection.features.can_return_id_from_insert = False
        #print "save"

        #print "name is",self.name, "=================== active is", self.active
        self.full_clean()
        super(StudentGroup, self).save(*args, **kwargs)

class Student(models.Model):
    ''' This class gives information regarding the students class , academic year and personnel details'''

    first_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    uid = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(max_length=20,null=True)
    gender = models.CharField(max_length=10, choices=GENDER,
                              default='male')
    mt = models.ForeignKey(MoiType, default='1')
    active = models.IntegerField(blank=True, null=True, default=2)
    
    class Meta:

        ordering = ['first_name', 'middle_name', 'last_name']
    
    def __unicode__(self):
        return '%s' % self.first_name


    def get_relations(self):
        return Relations.objects.filter(student_id=self.id)

    def get_mother(self):
        return Relations.objects.filter(relation_type='Mother',
                student_id=self.id)
    
    def get_father(self):
        return Relations.objects.get(relation_type='Father',
                student_id=self.id)

    def get_student(self):
        return Student.objects.get(id=self.id)


    def get_name(self):
        return self.child.first_name

    def get_child(self):
        return False

    def get_all_academic_years(self):
        return AcademicYear.objects.all()

    def get_all_languages(self):
        return MoiType.objects.all()

    def getModuleName(self):
        return 'student'

    def save(self, *args, **kwargs):
        # custom save method
        #pdb.set_trace()
        from django.db import connection
        connection.features.can_return_id_from_insert = False
        #print "save"

        #print "active is", self.active
        self.full_clean()
        super(Student, self).save(*args, **kwargs)

class StudentStudentGroupRelation(models.Model):
    '''This Class stores the Student and Student Group Relation Information'''

    student = models.ForeignKey(Student)
    student_group = models.ForeignKey(StudentGroup)
    academic = models.ForeignKey(AcademicYear,
                                 default=current_academic)
    active = models.IntegerField(blank=True, null=True, default=2)

    class Meta:

        unique_together = (('student', 'student_group', 'academic'), )

    def save(self, *args, **kwargs):
        # custom save method
        #pdb.set_trace()
        from django.db import connection
        connection.features.can_return_id_from_insert = False
        #print "save"

        #print "active is", self.active
        self.full_clean()
        super(Student_StudentGroupRelation, self).save(*args, **kwargs)

class StaffStudentGroupRelation(models.Model):
    '''This Class stores the Staff and Student Group Relation Information'''

    staff = models.ForeignKey(Staff)
    student_group = models.ForeignKey(StudentGroup)
    academic = models.ForeignKey(AcademicYear,
                                 default=current_academic)
    active = models.IntegerField(blank=True, null=True, default=2)

    class Meta:

        unique_together = (('staff', 'student_group', 'academic'), )

