from rest_framework import status
from rest_framework.test import APIClient, APIRequestFactory
from django.test import TestCase
from django.conf import settings
from schools.models import Student
import unittest
import json
import csv

class StudentsApiTestCase(TestCase):
    boundary_type_url = "/api/v1/boundarytype/"
    boundary_category_url="/api/v1/boundarycategory/"

    def setup(self):
        self.client = APIClient()

    def test_get_boundary_types(self):
        print "GET boundary types.."
        response = self.client.get(self.boundary_type_url)
        self.assertEqual(200, response.status_code)
        print response.data
        self.assertEqual(2, response.data['count'])
        results = response.data['results']
        self.assertTrue('boundary_type' in results[0])
        self.assertTrue('boundary_type' in results[1])
        self.assertTrue('id' in results[0])
        self.assertTrue('id' in results[1])

    def test_get_boundary_category(self):
        pass
        
        
