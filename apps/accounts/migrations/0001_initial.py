# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
from django.contrib.auth.models import Group , Permission


def forwards_func(apps, schema_editor):
    group = Group.objects.create(name="tada_admin")
    permissions = Permission.objects.all()
    for permission in permissions:
        group.permissions.add(permission)
    group = Group.objects.create(name="tada_deo")
    group = Group.objects.create(name="tada_dee")
        
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    # Country = apps.get_model("myapp", "Country")
    # db_alias = schema_editor.connection.alias
    # Country.objects.using(db_alias).bulk_create([
    #     Country(name="USA", code="us"),
    #     Country(name="France", code="fr"),
    # ])

def reverse_func(apps, schema_editor):
    Group.objects.get(name="tada_admin").delete()
    Group.objects.get(name="tada_deo").delete()
    Group.objects.get(name="tada_dee").delete()
    # forwards_func() creates two Country instances,
    # so reverse_func() should delete them.
    # Country = apps.get_model("myapp", "Country")
    # db_alias = schema_editor.connection.alias
    # Country.objects.using(db_alias).filter(name="USA", code="us").delete()
    # Country.objects.using(db_alias).filter(name="France", code="fr").delete()    


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
