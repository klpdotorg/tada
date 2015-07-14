from rest_framework import serializers

from .models import Institution, Student

class InstitutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Institution
        fields = ('name' ,)

class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = ('first_name' ,'middle_name', 'last_name' , 'uid', 'dob', 'gender' , 'mt', 'active')
