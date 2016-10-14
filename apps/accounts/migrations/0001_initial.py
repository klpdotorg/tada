# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
from django.contrib.auth.models import Group , Permission

# Initial migration for populating the db with groups and their permissions.

def forwards_func(apps, schema_editor):
    group = Group.objects.create(name="tada_admin")
    for permission in Permission.objects.all():
        group.permissions.add(permission)

    group = Group.objects.create(name="tada_deo")
    group = Group.objects.create(name="tada_dee")

def reverse_func(apps, schema_editor):
    Group.objects.get(name="tada_admin").delete()
    Group.objects.get(name="tada_deo").delete()
    Group.objects.get(name="tada_dee").delete()

class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
