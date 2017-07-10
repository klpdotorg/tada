from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from easyaudit.models import CRUDEvent

from .models import (
    Assessment,
    AnswerInstitution,
    AnswerStudent,
    AnswerStudentGroup,
    Boundary,
    BoundaryCategory,
    BoundaryType,
    Institution,
    InstitutionCategory,
    InstitutionManagement,
    MoiType,
    Programme,
    Question,
    Relations,
    Staff,
    Student,
    StudentGroup,
    StudentStudentGroupRelation,
    AssessmentInstitutionAssociation,
    AssessmentStudentGroupAssociation
)

from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin
)


class AnswerInstitutionSerializer(BulkSerializerMixin, serializers.ModelSerializer):

    class Meta:
        model = AnswerInstitution
        list_serializer_class = BulkListSerializer


class AnswerStudentSerializer(BulkSerializerMixin, serializers.ModelSerializer):

    history = serializers.SerializerMethodField()

    class Meta:
        model = AnswerStudent
        list_serializer_class = BulkListSerializer
        fields = (
            'id', 'question', 'student', 'answer_score', 'answer_grade',
            'double_entry', 'status', 'active', 'history'
        )


    def get_history(self, obj):
        history = {}

        if CRUDEvent.objects.filter(
                object_id=obj.id, event_type=CRUDEvent.CREATE).exists():
            history['created_by'] = CRUDEvent.objects.filter(
                object_id=obj.id,
                event_type=CRUDEvent.CREATE
            ).latest('id').user.id
        else:
            history['created_by'] = None

        if CRUDEvent.objects.filter(
                object_id=obj.id, event_type=CRUDEvent.UPDATE).exists():
            history['updated_by'] = CRUDEvent.objects.filter(
                object_id=obj.id,
                event_type=CRUDEvent.UPDATE
            ).latest('id').user.id
        else:
            history['updated_by'] = None

        return history


class AnswerStudentGroupSerializer(BulkSerializerMixin, serializers.ModelSerializer):

    class Meta:
        model = AnswerStudentGroup
        list_serializer_class = BulkListSerializer


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
        fields = ('id', 'name')


class BoundaryCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = BoundaryCategory
        fields = ('id', 'name')


class InstitutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Institution
        fields = (
            'id', 'boundary', 'dise_code', 'name', 'cat', 'institution_gender',
            'languages', 'mgmt', 'address', 'area', 'pincode', 'landmark',
            'active'
        )


class InstitutionCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = InstitutionCategory


class InstitutionManagementSerializer(serializers.ModelSerializer):

    class Meta:
        model = InstitutionManagement


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = MoiType


class AssessmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assessment
        fields = (
            'id', 'programme', 'name', 'start_date', 'end_date',
            'active', 'double_entry', 'type', 'institutions',
            'studentgroups', 'students',
        )
        read_only_fields = ('institutions', 'studentgroups', 'students')

class AssessmentInstitutionAssociationSerializer(serializers.ModelSerializer):

    class Meta:
        model = AssessmentInstitutionAssociation
        fiels = (
                'assessment', 'institution', 'active',
        )


class AssessmentStudentGroupAssociationSerializer(serializers.ModelSerializer):

    class Meta:
        model = AssessmentStudentGroupAssociation
        fiels = (
                'assessment', 'student_group', 'active',
        )


class ProgrammeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Programme
        fields = (
            'id', 'name', 'description', 'start_date', 'end_date',
            'programme_institution_category', 'active'
        )


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question


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
        list_serializer_class = BulkListSerializer


    def create(self, validated_data):
        studentgroup_id = self.context['view'].kwargs['parent_lookup_studentgroups']
        active = validated_data.get('active', 2)
        try:
            student_group = StudentGroup.objects.get(id=studentgroup_id)
        except:
            raise ValidationError(studengroup_id + " not found.")

        relations_data = validated_data.pop('relations')
        student = Student.objects.create(**validated_data)
        for item in relations_data:
            relation = Relations.objects.create(student=student,**item)
        student.save()

        student_studentgroup_relation, created = StudentStudentGroupRelation.objects.get_or_create(
            student=student,
            student_group=student_group,
            active=active,
        )

        return student

    def update(self, instance, validated_data):
        relations_data = validated_data.pop('relations')
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.middle_name = validated_data.get('middle_name',instance.middle_name)
        instance.last_name = validated_data.get('last_name',instance.last_name)
        instance.uid = validated_data.get('uid', instance.uid)
        instance.save()
        student_id = instance.id
        relations = Relations.objects.filter(student_id=instance.id)
        for item in relations_data:
            relation = Relations.objects.get(id=item['id'])
            #if firstname, lastname and middle name are empty, delete the relation
            relation.relation_type = item.get('relation_type')
            # If all the names are empty, delete the relation
            first_name = item.get('first_name')
            middle_name = item.get('middle_name')
            last_name = item.get('last_name')
            if not first_name and not middle_name and not last_name:
                relation.delete()
            else:
                relation.first_name = item.get('first_name')
                relation.middle_name = item.get('middle_name')
                relation.last_name = item.get('last_name')
                relation.save()
        instance.save()
        return instance


class StudentGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentGroup
        fields = (
            'id', 'institution', 'name', 'section', 'active', 'group_type'
        )

class StudentStudentGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentStudentGroupRelation
        fields = (
            'id','student','student_group','academic','active'
        )


class StaffSerializer(serializers.ModelSerializer):

    class Meta:
        model = Staff
        fields = (
            'id','first_name', 'middle_name', 'last_name', 'institution',
            'doj', 'gender', 'mt', 'qualification', 'active'
        )
