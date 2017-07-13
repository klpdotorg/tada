#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from .institution import Institution


GENDER = [('male', 'male'), ('female', 'female')]


class Teacher(models.Model):
    ''' Class representing a teacher in an Institution'''

    institution = models.ForeignKey(Institution)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(
        max_length=10, choices=GENDER, default='male'
    )
    qualification = models.CharField(max_length=100, blank=True, null=True)
    total_work_experience_years = models.IntegerField(
        default=0, blank=True, null=True
    )
    total_work_experience_months = models.IntegerField(
        default=0, blank=True, null=True
    )
    subject = models.CharField(max_length=100, blank=True, null=True)
    contact_no = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=1000, blank=True, null=True)
    area = models.CharField(max_length=200, blank=True, null=True)
    pincode = models.CharField(max_length=100, blank=True, null=True)
    active = models.IntegerField(default=2)

    def __unicode__(self):
        return '%s' % self.first_name
