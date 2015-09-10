from rest_framework import serializers

from .models import (
    Institution, Student, Relations, AssessmentInstitution,
    ProgrammeInstitution, Boundary, Staff
)


class InstitutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Institution
        fields = (
            'id', 'boundary', 'dise_code', 'name', 'cat', 'institution_gender',
            'languages', 'mgmt', 'address', 'area', 'pincode', 'landmark',
            'active'
        )


class AssessmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = AssessmentInstitution
        fields = (
            'id', 'programme', 'name', 'start_date', 'end_date', 'query',
            'active', 'double_entry', 'flexi_assessment', 'primary_field_name',
            'PRIMARY_FIELD_TYPE'
        )


class ProgrammeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProgrammeInstitution
        fields = (
            'id', 'name', 'description', 'start_date', 'end_date',
            'programme_institution_category', 'active'
        )


class BoundarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Boundary
        fields = (
            'id', 'parent', 'name', 'boundary_category', 'boundary_type',
            'active'
        )


class RelationsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Relations
        fields = (
            'relation_type', 'first_name' ,'middle_name', 'last_name'
        )

    def create(self, validated_data):
        print "Relations create"


class StudentSerializer(serializers.ModelSerializer):
    
    relations = RelationsSerializer(many='True')
    class Meta:
        model = Student
        fields = (
            'first_name', 'middle_name', 'last_name', 'uid', 'dob', 'gender',
            'mt', 'active', 'relations'
        )

    def create(self, validated_data):
        
        relations_data=validated_data.pop('relations')
        print "Relations data is: "
        print relations_data
        student=Student.objects.create(**validated_data)
        print 'created student object'
        for item in relations_data:
            print item
            relation = Relations.objects.create(student=student,**item)
            print "Done creating relation"
            relation.save()            
        student.save()
        return student


class StaffSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Staff
        fields = (
            'first_name', 'middle_name', 'last_name', 'institution', 'doj', 'gender',
            'mt', 'qualification', 'active'
        )
