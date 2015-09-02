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
    student_details_url = "/api/v1/students/"

    def setup(self):
        self.client = APIClient()
        '''Students.object.create(first_name="Amish", last_name="Trip", dob="20/08/2004", gender="male")'''

    def test_list_students(self):
        print "Testing student listing.."
        response = self.client.get(self.students_list_url)
        self.assertEqual(
            response.status_code, 200,
            "Students list URL returned:  %s" % response.status_code
        )
        print response.data

    def test_student_details(self):
        print "Testing student details.."
        query_url= self.student_details_url + "430201/"
        print query_url
        response = self.client.get(query_url)
        print response.status_code
        data=json.loads(response.content)
        print data
        self.assertEqual(response.status_code, 200, "students detail URL returned: %s" % response.status_code)
        self.assertTrue('first_name' in data, "has property first name")
        self.assertTrue('middle_name' in data, "has property middle name")
        self.assertTrue('last_name' in data, "has property last name")
        self.assertTrue('uid' in data, "has property uid")
        self.assertTrue('dob' in data, "has property dob")
        self.assertTrue()

    def test_post_new_student(self):
        pass

    def test_edit_student(self):
        pass

    def test_delete_student(self):
        pass

    def test_bulk_create(self):
        pass

    def test_bulk_edit(self):
        pass

    def test_bulk_delete(self):
        pass
        