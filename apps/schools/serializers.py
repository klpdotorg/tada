from rest_framework import serializers

from .models import (
    Institution, Student, Relations, AssessmentInstitution
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


class RelationsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Relations
        fields = (
            'relation_type', 'first_name' ,'middle_name', 'last_name'
        )


class StudentSerializer(serializers.ModelSerializer):
    
    relations = RelationsSerializer(many='True', source='get_relations')
    class Meta:
        model = Student
        fields = (
            'first_name', 'middle_name', 'last_name', 'uid', 'dob', 'gender',
            'mt', 'active', 'relations'
        )
