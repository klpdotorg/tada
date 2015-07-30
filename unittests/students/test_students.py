from rest_framework import status
from rest_framework.test import APILiveServerTestCase, APIClient
from django.conf import settings
from schools.models import Student
import unittest
import json
import csv


class StudentsApiTestCase(APILiveServerTestCase):

    students_base_url = "/api/v1/students/"

    def setup(self):
        self.client = APIClient()
        Students.object.create(first_name="Amish", last_name="Trip", dob="20/08/2004", gender="male")

    def test_list_students(self):
        print "Testing student listing.."
        response = self.client.get(self.students_base_url)
        self.assertEqual(
            response.status_code, 200,
            "Students list URL returned:  %s" % response.status_code
        )
        print response.data

    def test_student_details(self):
        print "Testing student details.."
