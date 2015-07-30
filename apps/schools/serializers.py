from rest_framework import serializers

from .models import Institution, Student, Relations

class InstitutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Institution
        fields = ('name' ,)


class RelationsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Relations
        fields = ('relation_type', 'first_name' ,'middle_name', 'last_name')

class StudentSerializer(serializers.ModelSerializer):
    
    relations = RelationsSerializer(source='get_relations')
    class Meta:
        model = Student
        fields = ('first_name' ,'middle_name', 'last_name' , 'uid', 'dob', 'gender' , 'mt', 'active', 'relations')
