#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from .boundary import BoundaryType
import datetime
from .institution import default_end_date

class Programme(models.Model):
    """ This class Stores information about Programme """

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True,
                                   null=True)
    start_date = models.DateField(max_length=20,
                                 default=datetime.date.today)
    end_date = models.DateField(max_length=20, default=default_end_date)
    programme_institution_category = models.ForeignKey(BoundaryType,
            blank=True, null=True)#shivangi, why null or blank?
    active = models.IntegerField(blank=True, null=True, default=2)#Shivangi, why null or blank?

    class Meta:

        ordering = ['-start_date', '-end_date', 'name']

    def __unicode__(self):
        return '%s (%s-%s)' % (self.name, self.start_date.strftime('%Y'
                               ), self.end_date.strftime('%Y'))

    def get_view_url(self):
        return '/programme/%s/view/' % self.id

    def get_edit_url(self):
        return '/programme/%s/update/' % self.id

    def getModuleName(self):
        return 'programme'

