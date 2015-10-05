from rest_framework import status
from rest_framework.test import APIClient, APIRequestFactory
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
        

    def test_post_new_student(self):
        print 'Testing creation of new student..'
        data = {"first_name": "Please",
                    "middle_name": "Hope2",
                    "last_name": "Work",
                    "uid": "null",
                    "dob": "2006-10-05",
                    "gender": "male",
                    "mt": 1,
                    "active": 0,
                    "relations": [{"relation_type": "Mother","first_name": "Kay2"},
                                    {"relation_type": "Father","first_name": "Sha2"}]}
        json_data = json.dumps(data)
        print json_data
        response = self.client.post('/api/v1/students/',json_data,content_type='application/json')
        print response.status_code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('relations' in response.data)
        print response.data
        results = json.loads(response.content)
        print results['id']
        response = self.client.get(self.student_details_url + str(results['id']) + "/")
        print response.status_code
        print response.data
        print 'Deleting student'
        delete_url= '/api/v1/students/' + str(results['id']) +"/"
        response = self.client.delete(delete_url)
        print response.status_code
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_edit_basic_student(self):
        print 'Testing edit of student..'
        print "CREATE STUDENT"
        data = {"first_name": "Delete",
                    "middle_name": "Test",
                    "last_name": "Me",
                    "uid": "null",
                    "dob": "2006-10-05",
                    "gender": "male",
                    "mt": 1,
                    "active": 0,
                    "relations": [{"relation_type": "Mother","first_name": "DelMom"},
                                    {"relation_type": "Father","first_name": "DelDad"}]}
        json_data = json.dumps(data)
        print json_data
        response = self.client.post('/api/v1/students/',json_data,content_type='application/json')
        print response.status_code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('relations' in response.data)
        results = json.loads(response.content)
        student_id = results['id']
        print student_id
        print "DONE CREATING STUDENT"
        print "====================="
        relation_1= results['relations'][0]
        relation_id_1 = relation_1['id']
        relation_id_2 = results['relations'][1]['id']
        print "RElation ID 1 is: " + str(relation_id_1)
        print "relation ID2 is: " + str(relation_id_2)
        print "EDITING STUDENT"
        edit_url= '/api/v1/students/' + str(student_id)+"/"
        edited_data = {"first_name": "Delete",
                    "middle_name": "Test",
                    "last_name": "MODIFIED",
                    "uid": "null",
                    "dob": "2006-10-05",
                    "gender": "male",
                    "mt": 1,
                    "active": 0,
                    "relations": [{"id": str(relation_id_1),"relation_type": "Mother","first_name": "DelMom"},
                                    {"id": str(relation_id_2),"relation_type": "Father","first_name": "DelDad"}]}
        json_data = json.dumps(edited_data)
        response = self.client.put(edit_url,json_data,content_type='application/json')
        print response.status_code
        self.assertEqual(response.status_code, 200)
        print "RETRIEVE EDITED STUDENT"
        response = self.client.get(self.student_details_url + str(student_id) + "/")
        print response.status_code
        print response.data
        edited_student = json.loads(response.content)
        last_name=edited_student['last_name']
        self.assertEqual(last_name, "MODIFIED")
       
    def test_edit_student_relations(self):
        print 'Testing edit of student relations..'
        print "CREATE STUDENT"
        data = {"first_name": "Delete",
                    "middle_name": "Test",
                    "last_name": "Me",
                    "uid": "null",
                    "dob": "2006-10-05",
                    "gender": "male",
                    "mt": 1,
                    "active": 0,
                    "relations": [{"relation_type": "Mother","first_name": "DelMom"},
                                    {"relation_type": "Father","first_name": "DelDad"}]}
        json_data = json.dumps(data)
        print json_data
        response = self.client.post('/api/v1/students/',json_data,content_type='application/json')
        print response.status_code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('relations' in response.data)
        results = json.loads(response.content)
        student_id = results['id']
        print student_id
        print "DONE CREATING STUDENT"
        print "====================="
        relation_1= results['relations'][0]
        relation_id_1 = relation_1['id']
        relation_id_2 = results['relations'][1]['id']
        print "RElation ID 1 is: " + str(relation_id_1)
        print "relation ID2 is: " + str(relation_id_2)
        print "EDITING STUDENT RELATIONS"
        edit_url= '/api/v1/students/' + str(student_id)+"/"
        edited_data = {
                    "id": str(student_id),
                    "first_name": "Delete",
                    "middle_name": "Test",
                    "last_name": "MODIFIED",
                    "uid": "null",
                    "dob": "2006-10-05",
                    "gender": "male",
                    "mt": 1,
                    "active": 0,
                    "relations": [{"id": str(relation_id_1), 
                                    "relation_type": "Mother","first_name": "ModifiedMom"},
                                    {"id": str(relation_id_2), "relation_type": "Father","first_name": "ModifiedDad"}]}
        json_data = json.dumps(edited_data)
        response = self.client.put(edit_url,json_data,content_type='application/json')
        print response.status_code
        self.assertEqual(response.status_code, 200)
        print "RETRIEVE EDITED STUDENT"
        response = self.client.get(self.student_details_url + str(student_id) + "/")
        print response.status_code
        edited_student = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        edited_relations = edited_student['relations']
        # Need to check ordering here
        edited_mothers_name=edited_relations[0]['first_name']
        edited_fathers_name =edited_relations[1]['first_name']
        self.assertEqual("ModifiedMom", edited_mothers_name)
        self.assertEqual("ModifiedDad", edited_relations[1]['first_name'])
        
    def test_delete_student_relations(self):
        print 'Testing edit of student relations..'
        print "CREATE STUDENT"
        data = {"first_name": "Delete",
                    "middle_name": "Test",
                    "last_name": "Me",
                    "uid": "null",
                    "dob": "2006-10-05",
                    "gender": "male",
                    "mt": 1,
                    "active": 0,
                    "relations": [{"relation_type": "Mother","first_name": "DelMom"},
                                    {"relation_type": "Father","first_name": "DelDad"}]}
        json_data = json.dumps(data)
        response = self.client.post('/api/v1/students/',json_data,content_type='application/json')
        print response.status_code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('relations' in response.data)
        self.assertTrue('id' in response.data)
        results = json.loads(response.content)
        student_id = results['id']
        print "DONE CREATING STUDENT"
        print "====================="
        relation_1= results['relations'][0]
        relation_id_1 = relation_1['id']
        relation_id_2 = results['relations'][1]['id']
        print "EDITING STUDENT RELATIONS"
        edit_url= '/api/v1/students/' + str(student_id)+"/"
        #Pass empty first_name and last_name for relations and it'll get deleted on the server
        edited_data = {
                    "id": str(student_id),
                    "first_name": "Delete",
                    "middle_name": "Test",
                    "last_name": "MODIFIED",
                    "uid": "null",
                    "dob": "2006-10-05",
                    "gender": "male",
                    "mt": 1,
                    "active": 0,
                    "relations": [{"id": str(relation_id_1), 
                                    "relation_type": "Mother","first_name": " "},
                                    {"id": str(relation_id_2), "relation_type": "Father","first_name": " "}]}
        json_data = json.dumps(edited_data)
        response = self.client.put(edit_url,json_data,content_type='application/json')
        print response.status_code
        print response.content
        self.assertEqual(response.status_code, 200)
        print "RETRIEVE EDITED STUDENT"
        response = self.client.get(self.student_details_url + str(student_id) + "/")
        print response.status_code
        edited_student = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        edited_relations = edited_student['relations']
        print edited_relations
        #Assert that it is empty
        self.assertFalse(edited_relations)

    def test_delete_student(self):
        print "Testing deletion of student..."
        delete_url = '/api/v1/students/'
        data = {"first_name": "Delete",
                    "middle_name": "Test",
                    "last_name": "Me",
                    "uid": "null",
                    "dob": "2006-10-05",
                    "gender": "male",
                    "mt": 1,
                    "active": 0,
                    "relations": [{"relation_type": "Mother","first_name": "DelMom"},
                                    {"relation_type": "Father","first_name": "DelDad"}]}
        json_data = json.dumps(data)
        print json_data
        response = self.client.post('/api/v1/students/',json_data,content_type='application/json')
        print response.status_code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('relations' in response.data)
        results = json.loads(response.content)
        student_id = results['id']
        print student_id
        print "DONE CREATING STUDENT"
        print "====================="
        delete_url = delete_url + str(student_id) + "/"
        print delete_url
        response = self.client.delete(delete_url)
        print response.status_code
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_bulk_create(self):
        print 'Testing bulk create..'
        data = [{"first_name": "Bulk1",
                    "middle_name": "Middle1",
                    "last_name": "Create1",
                    "uid": "null",
                    "dob": "2002-11-05",
                    "gender": "male",
                    "mt": 1,
                    "active": 0,
                    "relations": [{"relation_type": "Mother","first_name": "BulkMom1"},
                                    {"relation_type": "Father","first_name": "BulkDad1"}]},
                {"first_name": "Bulk2",
                    "middle_name": "Middle2",
                    "last_name": "Create2",
                    "uid": "null",
                    "dob": "2000-11-05",
                    "gender": "female",
                    "mt": 1,
                    "active": 0,
                    "relations": [{"relation_type": "Mother","first_name": "BulkMom2"},
                                    {"relation_type": "Father","first_name": "BulkDad2"}]},

                ]
        json_data = json.dumps(data)
        print json_data
        response = self.client.post('/api/v1/students/',json_data,content_type='application/json')
        print response.status_code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #self.assertTrue('relations' in response.data)
        print response.data
        results = json.loads(response.content)
        #print results['id']
        #response = self.client.get(self.student_details_url + str(results['id']) + "/")
        print response.status_code
        print response.data
        #print 'Deleting student'
        #delete_url= '/api/v1/students/' + str(results['id']) +"/"
        #response = self.client.delete(delete_url)
        #print response.status_code
        #self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_bulk_edit(self):
        pass

    def test_bulk_delete(self):
        pass
        