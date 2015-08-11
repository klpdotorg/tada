#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


class BoundaryCategory(models.Model):
    '''This Class stores the Boundary Category Information'''

    boundary_category = models.CharField(max_length=100)

    def __unicode__(self):
        return '%s' % self.boundary_category

class BoundaryType(models.Model):
    '''This Class stores the Boundary Type Information'''

    boundary_type = models.CharField(max_length=100)

    def __unicode__(self):
        return '%s' % self.boundary_type

class Boundary(models.Model):
    '''This class specifies the longitude and latitute of the area'''

    parent = models.ForeignKey('self', blank=True, null=True)
    name = models.CharField(max_length=300)
    boundary_category = models.ForeignKey(BoundaryCategory,
            blank=True, null=True)
    boundary_type = models.ForeignKey(BoundaryType, blank=True,
            null=True)
    active = models.IntegerField(blank=True, null=True, default=2)

    class Meta:
        """ Used For ordering """

        ordering = ['name']

    def __unicode__(self):
        return '%s' % self.name

    def getChild(self, boundaryType):
        if Boundary.objects.filter(parent__id=self.id, active=2,
                                   boundary_type=boundaryType).count():
            return True
        elif Institution.objects.filter(boundary__id=self.id,
                active=2).count():
            return True
        else:
            return False

    def getModuleName(self):
        return 'boundary'

    def get_view_url(self, boundaryType):
        return '/boundary/%s/%s/view/' % (self.id, boundaryType)

    def get_edit_url(self):
        return '/boundary/%s/update/' % self.id

    def get_update_url(self):
        return '/boundary/%d/update/' % self.id

    def getPermissionChild(self, boundaryType):
        if Boundary.objects.filter(parent__id=self.id, active=2,
                                   boundary_type=boundaryType):
            return True
        else:
            return False
