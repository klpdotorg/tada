from rest_framework import serializers
from .models import (
    Institution, Student, Relations, AssessmentInstitution,
    ProgrammeInstitution, Boundary, Staff, BoundaryType, BoundaryCategory
)
from rest_framework_bulk import (
    BulkListSerializer, BulkSerializerMixin,)


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


class BoundaryTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = BoundaryType
        fields = ('id', 'boundary_type')


class BoundaryCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = BoundaryCategory
        fields = ('id', 'boundary_category')


class RelationsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Relations
        fields = (
            'id','relation_type', 'first_name' ,'middle_name', 'last_name'
        )
        list_serializer_class=BulkListSerializer
        # Added this so the relation id is propagated in PUTs to the student endpoint. Relation info is
        # nested in student info.
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }


class StudentSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    
    relations = RelationsSerializer(many='True')
    class Meta:
        model = Student
        fields = (
            'id', 'first_name', 'middle_name', 'last_name', 'uid', 'dob', 'gender',
            'mt', 'active', 'relations'
        )
        list_serializer_class=BulkListSerializer


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
        student.save()
        return student

    def update(self, instance, validated_data):
        print "Validated data:" 
        print validated_data
        relations_data=validated_data.pop('relations')
        instance.first_name=validated_data.get('first_name', instance.first_name)
        instance.middle_name=validated_data.get('middle_name',instance.middle_name)
        instance.last_name=validated_data.get('last_name',instance.last_name)
        instance.save()
        student_id = instance.id 
        relations = Relations.objects.filter(student_id=instance.id)
        for item in relations_data:
            print item
            relation = Relations.objects.get(id=item['id'])
            #if firstname, lastname and middle name are empty, delete the relation
            relation.relation_type = item.get('relation_type')       
            # If all the names are empty, delete the relation
            first_name=item.get('first_name')
            middle_name=item.get('middle_name')
            last_name=item.get('last_name')
            if not first_name and not middle_name and not last_name:
                relation.delete()
            else:
                relation.first_name=item.get('first_name')
                relation.middle_name=item.get('middle_name')
                relation.last_name=item.get('last_name')
                relation.save()
        instance.save()
        return instance


class StaffSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Staff
        fields = (
            'id','first_name', 'middle_name', 'last_name', 'institution',
            'doj', 'gender', 'mt', 'qualification', 'active'
        )
