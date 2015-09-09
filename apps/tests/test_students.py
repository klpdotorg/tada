from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase
from django.conf import settings
from schools.models import Student
import unittest
import json
import csv


class StudentsApiTestCase(TestCase):

    students_list_url = "/api/v1/students/"
    student_details_url = "/api/v1/student/"

    def setup(self):
        self.client = APIClient()
        '''Students.object.create(first_name="Amish", last_name="Trip", dob="20/08/2004", gender="male")'''

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
        query_url= self.student_details_url + "429883"
        response = self.client.get(query_url)
        self.assertEqual(response.status_code, 200, "students detail URL returned: %s" % response.status_code)
        print response.data