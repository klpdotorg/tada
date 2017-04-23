#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
import datetime
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User
from .boundary import Boundary, BoundaryCategory, BoundaryType

PRIMARY_FIELD_TYPE = [(0, 'Default'),(1, 'Integer'), (2, 'Char'), (3, 'Date'), (4,
                      'Lookup')]
GENDER = [('male', 'male'), ('female', 'female')]

INSTITUTION_GENDER = [('boys', 'boys'), ('girls', 'girls'), ('co-ed',
                      'co-ed')]

class InstitutionCategory(models.Model):
    '''This Class stores the Institution Category Information'''

    name = models.CharField(max_length=50)
    category_type = models.IntegerField()

    def __unicode__(self):
        return '%s' % self.name


class MoiType(models.Model):
    '''This Class stores the Mother Toungue (Languages) Information'''

    name = models.CharField(max_length=50)

    def __unicode__(self):
        return '%s' % self.name


class InstitutionManagement(models.Model):
    '''This Class stores the Institution Management Information'''

    name = models.CharField(max_length=50)

    def __unicode__(self):
        return '%s' % self.name



class StaffType(models.Model):
    '''This Class stores information about Staff Type'''

    staff_type = models.CharField(max_length=100)
    category_type = models.IntegerField()

    def __unicode__(self):
        return '%s' % self.staff_type


class QualificationList(models.Model):
    ''' This Class Stores Information about staff qualification '''

    qualification = models.CharField(max_length=100)

    def __unicode__(self):
        return '%s' % self.qualification


class Institution(models.Model):
    ''' It stores the all data regarding Institutions'''

    boundary = models.ForeignKey(Boundary)
    dise_code = models.CharField(max_length=14, blank=True, null=True)
    name = models.CharField(max_length=300)
    cat = models.ForeignKey(InstitutionCategory, blank=True, null=True)
    institution_gender = models.CharField(max_length=10,
            choices=INSTITUTION_GENDER, default='co-ed')
    languages = models.ManyToManyField(MoiType)
    mgmt = models.ForeignKey(InstitutionManagement, default='1')
    address = models.CharField(max_length=1000, blank=True, null=True)
    area = models.CharField(max_length=200, blank=True, null=True)
    pincode = models.CharField(max_length=100, blank=True, null=True)
    landmark = models.CharField(max_length=1000, blank=True, null=True,
                                help_text='Can be comma separated')
    instidentification = models.CharField(max_length=1000, blank=True,
            null=True, help_text='Can be comma separated')
    instidentification2 = models.CharField(max_length=1000, blank=True,
            null=True, help_text='Can be comma separated')
    route_information = models.CharField(max_length=500, blank=True,
            null=True, help_text='Can be comma separated')
    active = models.IntegerField(blank=True, null=True, default=2)

    class Meta:
        ordering = ['name']
        permissions = (
            ('crud_student_class_staff', 'CRUD Student Class and Staff'),
        )

    def __unicode__(self):
        return '%s' % self.name

    def get_all_cat(self, category_type):
        return InstitutionCategory.objects.all(category_type=category_type)

    def getChild(self):
        if StudentGroup.objects.filter(institution__id=self.id,
                active=2).count():
            return True
        else:
            return False

    def get_all_mgmt(self):
        return institution_Management.objects.all()

    def get_all_languages(self):
        return MoiType.objects.all()

    def getModuleName(self):
        return 'institution'

    def get_update_url(self):
        return '/institution/%d/update/' % self.id

    def get_view_url(self):
        return '/institution/%s/view/' % self.id

    def get_edit_url(self):
        return '/institution/%s/update/' % self.id

from django.db.models.signals import post_save, pre_save


class AcademicYear(models.Model):
    ''' Its stores the academic years information'''

    name = models.CharField(max_length=20, unique=True)
    active = models.IntegerField(blank=True, null=True, default=0)
    start_year = models.IntegerField(blank=True, null=False, default=0)
    end_year = models.IntegerField(blank=True, null=False,default=0)
    def __unicode__(self):
        return self.name


class Staff(models.Model):
    '''This Class stores the Institution Worker(Staff) Information'''

    institution = models.ForeignKey(Institution, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    doj = models.DateField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER,
                              default='female')
    mt = models.ForeignKey(MoiType, default=1)
    uid = models.CharField(max_length=100, blank=True, null=True)

    qualification = models.ManyToManyField(QualificationList,
            blank=True)
    staff_type = models.ForeignKey(StaffType, default=1)
    active = models.IntegerField(blank=True, null=True, default=2)

    def __unicode__(self):
        return '%s %s %s' % (self.first_name, self.middle_name, self.last_name)

    def getAssigendClasses(self):
        return StudentGroup.objects.filter(
            staff_studentgrouprelation__staff__id=self.id,
            staff_studentgrouprelation__active=2)


def current_academic():
    ''' To select current academic year'''
    try:
        academicObj = AcademicYear.objects.get(active=1)
        return academicObj
    except AcademicYear.DoesNotExist:
        return 1

def default_end_date():
    ''' To select academic year end date'''

    now = datetime.date.today()
    currentYear = int(now.strftime('%Y'))
    currentMont = int(now.strftime('%m'))
    academicYear = current_academic().name
    academicYear = academicYear.split('-')
    if currentMont > 5 and int(academicYear[0]) == currentYear:
        academic_end_date = datetime.date(currentYear+1, 5, 30)
    else:
        academic_end_date = datetime.date(currentYear, 5, 30)
    return academic_end_date


def call(sender, method, instance):
    func = getattr(sender, method, None)
    if callable(func):
        func(instance)

def post_save_hook(sender, **kwargs):
    if kwargs['created']:
        call(sender, 'after_create', kwargs['instance'])
        if kwargs['instance'].boundary_type.id == 2:
            a=BoundaryCategory.objects.get(id=13)
            obj = Boundary.objects.get(id=kwargs['instance'].id)
            if obj.parent.id == 1:
                obj.boundary_category = a
                obj.save()
    else:
        call(sender, 'after_update', kwargs['instance'])
    call(sender, 'after_save', kwargs['instance'])

post_save.connect(post_save_hook, sender=Boundary)

