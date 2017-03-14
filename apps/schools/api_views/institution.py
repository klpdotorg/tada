from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework_extensions.mixins import NestedViewSetMixin
from django.db.models import F

from guardian.shortcuts import assign_perm, get_users_with_perms

from accounts.permissions import (
    AssessmentPermission,
    InstitutionCreateUpdatePermission,
    WorkUnderInstitutionPermission,
)

from schools.filters import (
    AssessmentFilter,
    BoundaryFilter,
    InstitutionFilter,
    ProgrammeFilter,
    QuestionFilter
)

from schools.serializers import (
    AssessmentSerializer,
    AnswerInstitutionSerializer,
    BoundarySerializer,
    BoundaryCategorySerializer,
    BoundaryTypeSerializer,
    InstitutionSerializer,
    InstitutionCategorySerializer,
    InstitutionManagementSerializer,
    LanguageSerializer,
    ProgrammeSerializer,
    QuestionSerializer,
    StaffSerializer,
)

from schools.models import (
    Assessment,
    AssessmentStudentGroupAssociation,
    AssessmentInstitutionAssociation,
    AnswerInstitution,
    Boundary,
    BoundaryCategory,
    BoundaryType,
    Institution,
    InstitutionCategory,
    InstitutionManagement,
    MoiType,
    Programme,
    Question,
    Staff,
)
import sys


class AssessmentListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    filter_class = AssessmentFilter


class AssessmentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    permission_classes = (AssessmentPermission,)
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    filter_class = AssessmentFilter


class AnswerInstitutionViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    # permission_classes = (AssessmentPermission,)
    queryset = AnswerInstitution.objects.all()
    serializer_class = AnswerInstitutionSerializer
    # filter_class = AnswerInstitutionFilter


class BoundaryViewSet(viewsets.ModelViewSet):
    queryset = Boundary.objects.all()
    serializer_class = BoundarySerializer
    filter_class = BoundaryFilter


class BoundaryCategoryViewSet(viewsets.ModelViewSet):
    queryset = BoundaryCategory.objects.all()
    serializer_class = BoundaryCategorySerializer


class BoundaryTypeViewSet(viewsets.ModelViewSet):
    queryset = BoundaryType.objects.all()
    serializer_class = BoundaryTypeSerializer


class InstitutionViewSet(viewsets.ModelViewSet):
    permission_classes = (InstitutionCreateUpdatePermission,)
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    filter_class = InstitutionFilter

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        self._assign_permissions(serializer.instance)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def _assign_permissions(self, institution):
        users_to_be_permitted = get_users_with_perms(institution.boundary)
        for user_to_be_permitted in users_to_be_permitted:
            assign_perm('change_institution', user_to_be_permitted, institution)
            assign_perm('crud_student_class_staff', user_to_be_permitted, institution)


class InstitutionCategoryViewSet(viewsets.ModelViewSet):
    queryset = InstitutionCategory.objects.all()
    serializer_class = InstitutionCategorySerializer


class InstitutionManagementViewSet(viewsets.ModelViewSet):
    queryset = InstitutionManagement.objects.all()
    serializer_class = InstitutionManagementSerializer


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = MoiType.objects.all()
    serializer_class = LanguageSerializer


class ProgrammeViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Programme.objects.all()
    serializer_class = ProgrammeSerializer
    filter_class = ProgrammeFilter
    programmeinfo = {}

    def retrieve(self, request, *args, **kwargs):
        pid = kwargs["pk"]
        self.programmeinfo = Programme.objects.get(id=pid)
        if request.GET.get('details'):
            programmeDetails = {}
            programmeDetails["info"] = ProgrammeSerializer(self.programmeinfo).data
            programmeDetails["details"] = self.getDetails(pid)
            return Response(programmeDetails)
        else:
            return Response(ProgrammeSerializer(self.programmeinfo).data)

    def getDetails(self,pid):
        programmeInfo = {}
        assessments = Assessment.objects.filter(programme_id=pid)
        for assessment in assessments:
            if assessment.type == 1: #institution assessment
                groups = AssessmentInstitutionAssociation.objects.filter(assessment=assessment.id).annotate(inst_name=F('institution__name'),inst_id=F('institution__id'),admin3_id=F('institution__boundary'),admin3_name=F('institution__boundary__name'),admin2_id=F('institution__boundary__parent'), admin2_name=F('institution__boundary__parent__name'),admin1_id=F('institution__boundary__parent__parent'),admin1_name=F('institution__boundary__parent__parent__name')).values('inst_id','inst_name','admin1_id','admin1_name','admin2_id','admin2_name','admin3_id','admin3_name')
                for group in groups:
                    if group["admin1_id"] not in programmeInfo:
                        programmeInfo[group["admin1_id"]]={"id":group["admin1_id"],"name":
                                group["admin1_name"],"boundaries":{group["admin2_id"]:{"id":group["admin2_id"],"name":group["admin2_name"],"boundaries":{group["admin3_id"]:{"id":group["admin3_id"],"name":group["admin3_name"],"institutions":{group["inst_id"]:{"id":group["inst_id"],"name":group["inst_name"],"assessments":{assessment.id:{"name":assessment.name,"id":assessment.id}}}}}}}}}
                    elif group["admin2_id"] not in programmeInfo[group["admin1_id"]]["boundaries"]:
                     programmeInfo[group["admin1_id"]]["boundaries"][group["admin2_id"]]={"id":group["admin2_id"],"name":group["admin2_name"],"boundaries":{group["admin3_id"]:{"id":group["admin3_id"],"name":group["admin3_name"],"institutions":{group["inst_id"]:{"id":group["inst_id"],"name":group["inst_name"],"assessments":{assessment.id:{"id":assessment.id,"name":assessment.name}}}}}}}
                    elif group["admin3_id"] not in programmeInfo[group["admin1_id"]]["boundaries"][group["admin2_id"]]["boundaries"]:
                     programmeInfo[group["admin1_id"]]["boundaries"][group["admin2_id"]]["boundaries"][group["admin3_id"]]={"id":group["admin3_id"],"name":group["admin3_name"],"institutions":{group["inst_id"]:{"id":group["inst_id"],"name":group["inst_name"],"assessments":{assessment.id:{"id":assessment.id,"name":assessment.name}}}}}
                    elif group["inst_id"] not in programmeInfo[group["admin1_id"]]["boundaries"][group["admin2_id"]]["boundaries"][group["admin3_id"]]["institutions"]:
                     programmeInfo[group["admin1_id"]]["boundaries"][group["admin2_id"]]["boundaries"][group["admin3_id"]]["institutions"][group["inst_id"]]={"id":group["inst_id"],"name":group["inst_name"],"assessments":{assessment.id:{"name":assessment.name,"assessment_id":assessment.id}}}
                    else:
                       programmeInfo[group["admin1_id"]]["boundaries"][group["admin2_id"]]["boundaries"][group["admin3_id"]]["institutions"][group["inst_id"]]["assessments"][assessment.id]={"name":assessment.name,"assessment_id":assessment.id}
            else:
                groups = AssessmentStudentGroupAssociation.objects.filter(assessment=assessment.id).annotate(sgid=F('student_group__id'),sgname=F('student_group__name'),inst_name=F('student_group__institution__name'),inst_id=F('student_group__institution__id'),admin3_id=F('student_group__institution__boundary'),admin3_name=F('student_group__institution__boundary__name'),admin2_id=F('student_group__institution__boundary__parent'), admin2_name=F('student_group__institution__boundary__parent__name'),admin1_id=F('student_group__institution__boundary__parent__parent'),admin1_name=F('student_group__institution__boundary__parent__parent__name')).values('sgid','sgname','inst_id','inst_name','admin1_id','admin1_name','admin2_id','admin2_name','admin3_id','admin3_name')
                for group in groups:
                    if group["admin1_id"] not in programmeInfo:
                        programmeInfo[group["admin1_id"]]={"id":group["admin1_id"],"name":
                                group["admin1_name"],"boundaries":{group["admin2_id"]:{"id":group["admin2_id"],"name":group["admin2_name"],"boundaries":{group["admin3_id"]:{"id":group["admin3_id"],"name":group["admin3_name"],"institutions":{group["inst_id"]:{"id":group["inst_id"],"name":group["inst_name"],"classes":{group["sgid"]:{"id":group["sgid"],"name":group["sgname"],"assessments":{assessment.id:{"name":assessment.name,"id":assessment.id}}}}}}}}}}}
                    elif group["admin2_id"] not in programmeInfo[group["admin1_id"]]["boundaries"]:
                     programmeInfo[group["admin1_id"]]["boundaries"][group["admin2_id"]]={"id":group["admin2_id"],"name":group["admin2_name"],"boundaries":{group["admin3_id"]:{"id":group["admin3_id"],"name":group["admin3_name"],"institutions":{group["inst_id"]:{"id":group["inst_id"],"name":group["inst_name"],"classes":{group["sgid"]:{"id":group["sgid"],"name":group["sgname"],"assessments":{assessment.id:{"id":assessment.id,"name":assessment.name}}}}}}}}}
                    elif group["admin3_id"] not in programmeInfo[group["admin1_id"]]["boundaries"][group["admin2_id"]]["boundaries"]:
                     programmeInfo[group["admin1_id"]]["boundaries"][group["admin2_id"]]["boundaries"][group["admin3_id"]]={"id":group["admin3_id"],"name":group["admin3_name"],"institutions":{group["inst_id"]:{"id":group["inst_id"],"name":group["inst_name"],"classes":{group["sgid"]:{"id":group["sgid"],"name":group["sgname"],"assessments":{assessment.id:{"id":assessment.id,"name":assessment.name}}}}}}}
                    elif group["inst_id"] not in programmeInfo[group["admin1_id"]]["boundaries"][group["admin2_id"]]["boundaries"][group["admin3_id"]]["institutions"]:
                     programmeInfo[group["admin1_id"]]["boundaries"][group["admin2_id"]]["boundaries"][group["admin3_id"]]["institutions"][group["inst_id"]]={"id":group["inst_id"],"name":group["inst_name"],"classes":{group["sgid"]:{"id":group["sgid"],"name":group["sgname"],"assessments":{assessment.id:{"name":assessment.name,"assessment_id":assessment.id}}}}}
                    elif group["sgid"] not in programmeInfo[group["admin1_id"]]["boundaries"][group["admin2_id"]]["boundaries"][group["admin3_id"]]["institutions"][group["inst_id"]]["classes"]:
                     programmeInfo[group["admin1_id"]]["boundaries"][group["admin2_id"]]["boundaries"][group["admin3_id"]]["institutions"][group["inst_id"]]["classes"][group["sgid"]]={"id":group["sgid"],"name":group["sgname"],"assessments":{assessment.id:{"name":assessment.name,"assessment_id":assessment.id}}}
                    else:
                       programmeInfo[group["admin1_id"]]["boundaries"][group["admin2_id"]]["boundaries"][group["admin3_id"]]["institutions"][group["inst_id"]]["classes"][group["sgid"]]["assessments"][assessment.id]={"name":assessment.name,"assessment_id":assessment.id}

        return programmeInfo


class QuestionViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_class = QuestionFilter


class StaffViewSet(viewsets.ModelViewSet):
    permission_classes = (WorkUnderInstitutionPermission,)
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

