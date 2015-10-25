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

class CompensationAuditLog(models.Model):
    """ This class stores audit information of changes to EMS """
    user = models.CharField(max_length=100)
    audit_time = models.DateField(default=datetime.date.today, max_length=20)
    entity_name = models.CharField(max_length=100)
    operation_type = models.CharField(max_length=20)
    operation_value = models.CharField(max_length=20)

    def __unicode__(self):
        return '%s' % self.user


