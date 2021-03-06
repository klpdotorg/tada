from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.exceptions import ParseError

from django.db.models import F
from django.db.models import Q
from django.http import Http404
from django.contrib.auth.models import User, Group

from guardian.shortcuts import (
    assign_perm,
    get_users_with_perms,
    get_objects_for_user,
)

from accounts.permissions import (
    InstitutionCreateUpdatePermission,
    WorkUnderAssessmentPermission,
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
    AnswerStudentSerializer,
    AnswerStudentGroupSerializer,
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
    AssessmentInstitutionAssociationSerializer,
    AssessmentStudentGroupAssociationSerializer
)

from schools.models import (
    Assessment,
    AssessmentStudentGroupAssociation,
    AssessmentInstitutionAssociation,
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
    Staff,
    StudentGroup,
)

from schools.mixins import (
    BulkAnswerCreateModelMixin,
    AnswerUpdateModelMixin,
    CompensationLogMixin
)


class AssessmentListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    filter_class = AssessmentFilter


class AssessmentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    filter_class = AssessmentFilter


class AnswerInstitutionViewSet(
        NestedViewSetMixin, BulkAnswerCreateModelMixin,
        viewsets.ModelViewSet, CompensationLogMixin,
        AnswerUpdateModelMixin):
    permission_classes = (WorkUnderAssessmentPermission,)
    queryset = AnswerInstitution.objects.all()
    serializer_class = AnswerInstitutionSerializer
    # filter_class = AnswerInstitutionFilter

    def filter_queryset_by_parents_lookups(self, queryset):
        parents_query_dict = self.get_parents_query_dict()
        if parents_query_dict.get('institution', None):
            try:
                institution_id = parents_query_dict.get('institution')
                assessment_id = parents_query_dict.get(
                    'institution__assessmentinstitutionassociation__assessment')
                return queryset.filter(
                    institution=institution_id,
                    question__assessment=assessment_id
                ).distinct('id')
            except Exception as ex:
                raise APIException(ex)
        elif parents_query_dict:
            try:
                return queryset.filter(
                    **parents_query_dict
                ).order_by().distinct('id')
            except ValueError:
                raise Http404
        else:
            return queryset


class AnswerStudentViewSet(
        NestedViewSetMixin, BulkAnswerCreateModelMixin,
        viewsets.ModelViewSet, CompensationLogMixin,
        AnswerUpdateModelMixin):
    permission_classes = (WorkUnderAssessmentPermission,)
    queryset = AnswerStudent.objects.all()
    serializer_class = AnswerStudentSerializer
    # filter_class = AnswerStudentFilter

    def filter_queryset_by_parents_lookups(self, queryset):
        parents_query_dict = self.get_parents_query_dict()
        if parents_query_dict.get('student', None):
            try:
                student_id = parents_query_dict.get('student')
                assessment_id = parents_query_dict.get(
                    'student__studentgroup__asssessment')
                return queryset.filter(
                    student=student_id,
                    question__assessment=assessment_id
                ).distinct('id')
            except Exception as ex:
                raise APIException(ex)
        elif parents_query_dict:
            try:
                return queryset.filter(
                    **parents_query_dict
                ).order_by().distinct('id')
            except ValueError:
                raise Http404
        else:
            return queryset


class AnswerStudentGroupViewSet(
        NestedViewSetMixin, BulkAnswerCreateModelMixin,
        viewsets.ModelViewSet, CompensationLogMixin,
        AnswerUpdateModelMixin):
    permission_classes = (WorkUnderAssessmentPermission,)
    queryset = AnswerStudentGroup.objects.all()
    serializer_class = AnswerStudentGroupSerializer
    # filter_class = AnswerStudentGroupFilter

    def filter_queryset_by_parents_lookups(self, queryset):
        parents_query_dict = self.get_parents_query_dict()
        if parents_query_dict.get('studentgroup', None):
            try:
                studentgroup_id = parents_query_dict.get('studentgroup')
                assessment_id = parents_query_dict.get(
                    'studentgroup__assessmentstudentgroupassociation__assessment'
                )
                return queryset.filter(
                    studentgroup=studentgroup_id,
                    question__assessment=assessment_id
                ).distinct('id')
            except Exception as ex:
                raise APIException(ex)
        elif parents_query_dict:
            try:
                return queryset.filter(
                    **parents_query_dict
                ).order_by().distinct('id')
            except ValueError:
                raise Http404
        else:
            return queryset


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


class InstitutionViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
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
            programmeDetails["details"] = self.getDetails(request, pid)
            return Response(programmeDetails)
        else:
            return Response(ProgrammeSerializer(self.programmeinfo).data)

    def getDetails(self, request, pid):
        programmeInfo = {}
        permitted_user = request.user
        tada_admin = Group.objects.get(name="tada_admin")
        if (
                permitted_user.is_superuser or
                permitted_user.groups.filter(id=tada_admin.id).exists()
        ):
            assessments = Assessment.objects.filter(programme_id=pid, active=2)
        else:
            assessments = get_objects_for_user(
                permitted_user, "crud_answers", klass=Assessment
            ).filter(
                programme_id=pid,
                active=2
            )
        for assessment in assessments:
            if assessment.type == 1:  # institution assessment
                groups = AssessmentInstitutionAssociation.objects.filter(
                    assessment=assessment.id).annotate(
                    inst_name=F('institution__name'),
                    inst_id=F('institution__id'),
                    admin3_id=F('institution__boundary'),
                    admin3_name=F('institution__boundary__name'),
                    admin2_id=F('institution__boundary__parent'),
                    admin2_name=F('institution__boundary__parent__name'),
                    admin1_id=F('institution__boundary__parent__parent'),
                    admin1_name=F('institution__boundary__parent__parent__name')
                    ).values('inst_id', 'inst_name', 'admin1_id', 'admin1_name',
                             'admin2_id', 'admin2_name', 'admin3_id', 'admin3_name')
                for group in groups:
                    if group["admin1_id"] not in programmeInfo:
                        programmeInfo[group["admin1_id"]] = {
                            "id": group["admin1_id"],
                            "name": group["admin1_name"],
                            "boundaries": {group["admin2_id"]: {
                                "id": group["admin2_id"],
                                "name": group["admin2_name"],
                                "boundaries": {group["admin3_id"]: {
                                    "id": group["admin3_id"],
                                    "name": group["admin3_name"],
                                    "institutions": {group["inst_id"]: {
                                        "id": group["inst_id"],
                                        "name": group["inst_name"],
                                        "assessments": {assessment.id: {
                                            "name": assessment.name,
                                            "id": assessment.id}}}}}}}}}
                    elif group["admin2_id"] not in programmeInfo[group["admin1_id"]]["boundaries"]:
                        programmeInfo[group["admin1_id"]]["boundaries"][group["admin2_id"]] = {
                            "id": group["admin2_id"],
                            "name": group["admin2_name"],
                            "boundaries": {group["admin3_id"]: {
                                "id": group["admin3_id"],
                                "name": group["admin3_name"],
                                "institutions": {group["inst_id"]: {
                                    "id": group["inst_id"],
                                    "name": group["inst_name"],
                                    "assessments": {assessment.id: {
                                        "id": assessment.id,
                                        "name": assessment.name}}}}}}}
                    elif group["admin3_id"] not in programmeInfo[group["admin1_id"]]["boundaries"][group["admin2_id"]]["boundaries"]:
                        programmeInfo[group["admin1_id"]]["boundaries"][group["admin2_id"]]["boundaries"][group["admin3_id"]] = {
                            "id": group["admin3_id"],
                            "name": group["admin3_name"],
                            "institutions": {group["inst_id"]: {
                                "id": group["inst_id"],
                                "name": group["inst_name"],
                                "assessments": {assessment.id: {
                                    "id": assessment.id,
                                    "name": assessment.name}}}}}
                    elif group["inst_id"] not in programmeInfo[group["admin1_id"]]["boundaries"][group["admin2_id"]]["boundaries"][group["admin3_id"]]["institutions"]:
                        programmeInfo[group["admin1_id"]]["boundaries"][group["admin2_id"]]["boundaries"][group["admin3_id"]]["institutions"][group["inst_id"]] = {
                            "id": group["inst_id"],
                            "name": group["inst_name"],
                            "assessments": {assessment.id: {
                                "name": assessment.name,
                                "id": assessment.id}}}
                    else:
                        programmeInfo[group["admin1_id"]]["boundaries"][group["admin2_id"]]["boundaries"][group["admin3_id"]]["institutions"][group["inst_id"]]["assessments"][assessment.id] = {
                            "name": assessment.name,
                            "id": assessment.id}
            else:
                groups = AssessmentStudentGroupAssociation.objects.filter(
                    assessment=assessment.id).annotate(
                    sgid=F('student_group__id'),
                    sgname=F('student_group__name'),
                    inst_name=F('student_group__institution__name'),
                    inst_id=F('student_group__institution__id'),
                    admin3_id=F('student_group__institution__boundary'),
                    admin3_name=F('student_group__institution__boundary__name'),
                    admin2_id=F('student_group__institution__boundary__parent'),
                    admin2_name=F('student_group__institution__boundary__parent__name'),
                    admin1_id=F('student_group__institution__boundary__parent__parent'),
                    admin1_name=F('student_group__institution__boundary__parent__parent__name')).values(
                    'sgid', 'sgname', 'inst_id', 'inst_name', 'admin1_id', 'admin1_name', 'admin2_id',
                    'admin2_name', 'admin3_id', 'admin3_name')
                for group in groups:
                    if group["admin1_id"] not in programmeInfo:
                        programmeInfo[group["admin1_id"]] = {
                            "id": group["admin1_id"],
                            "name": group["admin1_name"],
                            "boundaries": {group["admin2_id"]: {
                                "id": group["admin2_id"],
                                "name": group["admin2_name"],
                                "boundaries": {group["admin3_id"]: {
                                    "id": group["admin3_id"],
                                    "name": group["admin3_name"],
                                    "institutions": {group["inst_id"]: {
                                        "id": group["inst_id"],
                                        "name": group["inst_name"],
                                        "classes": {group["sgid"]: {
                                            "id": group["sgid"],
                                            "name": group["sgname"],
                                            "assessments": {assessment.id: {
                                                "name": assessment.name,
                                                "id": assessment.id}}}}}}}}}}}
                    elif group["admin2_id"] not in programmeInfo[group["admin1_id"]]["boundaries"]:
                        programmeInfo[group["admin1_id"]]["boundaries"][group["admin2_id"]] = {
                            "id": group["admin2_id"],
                            "name": group["admin2_name"],
                            "boundaries": {group["admin3_id"]: {
                                "id": group["admin3_id"],
                                "name": group["admin3_name"],
                                "institutions": {group["inst_id"]: {
                                    "id": group["inst_id"],
                                    "name": group["inst_name"],
                                    "classes": {group["sgid"]: {
                                        "id": group["sgid"],
                                        "name": group["sgname"],
                                        "assessments": {assessment.id: {
                                            "id": assessment.id,
                                            "name": assessment.name}}}}}}}}}
                    elif group["admin3_id"] not in programmeInfo[group["admin1_id"]]["boundaries"][group["admin2_id"]]["boundaries"]:
                        programmeInfo[group["admin1_id"]]["boundaries"][group["admin2_id"]]["boundaries"][group["admin3_id"]] = {
                            "id": group["admin3_id"],
                            "name": group["admin3_name"],
                            "institutions": {group["inst_id"]: {
                                "id": group["inst_id"],
                                "name": group["inst_name"],
                                "classes": {group["sgid"]: {
                                    "id": group["sgid"],
                                    "name": group["sgname"],
                                    "assessments": {assessment.id: {
                                        "id": assessment.id,
                                        "name": assessment.name}}}}}}}
                    elif group["inst_id"] not in programmeInfo[group["admin1_id"]]["boundaries"][group["admin2_id"]]["boundaries"][group["admin3_id"]]["institutions"]:
                        programmeInfo[group["admin1_id"]]["boundaries"][group["admin2_id"]]["boundaries"][group["admin3_id"]]["institutions"][group["inst_id"]] = {
                            "id": group["inst_id"],
                            "name": group["inst_name"],
                            "classes": {group["sgid"]: {
                                "id": group["sgid"],
                                "name": group["sgname"],
                                "assessments": {assessment.id: {
                                    "name": assessment.name,
                                    "id": assessment.id}}}}}
                    elif group["sgid"] not in programmeInfo[group["admin1_id"]]["boundaries"][group["admin2_id"]]["boundaries"][group["admin3_id"]]["institutions"][group["inst_id"]]["classes"]:
                        programmeInfo[group["admin1_id"]]["boundaries"][group["admin2_id"]]["boundaries"][group["admin3_id"]]["institutions"][group["inst_id"]]["classes"][group["sgid"]] = {
                            "id": group["sgid"],
                            "name": group["sgname"],
                            "assessments": {assessment.id: {
                                "name": assessment.name,
                                "id": assessment.id}}}
                    else:
                        programmeInfo[group["admin1_id"]]["boundaries"][group["admin2_id"]]["boundaries"][group["admin3_id"]]["institutions"][group["inst_id"]]["classes"][group["sgid"]]["assessments"][assessment.id] = {
                            "name": assessment.name,
                            "id": assessment.id}

        return programmeInfo


class QuestionViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_class = QuestionFilter


class StaffViewSet(viewsets.ModelViewSet):
    permission_classes = (WorkUnderInstitutionPermission,)
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class AssessmentStudentGroupAssociationViewSet(viewsets.ModelViewSet):
    assessmentids = []
    institutionids = []
    boundaryids = []
    studentgroups = []
    queryset = AssessmentStudentGroupAssociation.objects.all()
    serializer_class = AssessmentStudentGroupAssociationSerializer

    def create(self, request, *args, **kwargs):
        if not self.request.data.get('assessmentid'):
            raise ParseError("Mandatory parameter assessmentid not passed")
        self.assessmentids = self.request.data.get('assessmentid').split(",")
        if self.request.data.get('boundaryid'):
            self.boundaryids = self.request.data.get('boundaryid').split(",")
        if self.request.data.get('institutionid'):
            self.institutionids = self.request.data.get('institutionid').split(",")
        if self.institutionids == [] and self.boundaryids == []:
            raise ParseError("Mandatory parameter institution or boundary not passed")
        if not self.request.data.get('studentgroup'):
            raise ParseError("Mandatory parameter studentgroup not passed")
        self.studentgroups = self.request.data.get('studentgroup').split(",")
        response = self.createAssessmentStudentGroupAssocation()

        return response

    def createAssessmentStudentGroupAssocation(self):
        request = []
        for assessmentid in self.assessmentids:
            if self.institutionids == []:
                for boundaryid in self.boundaryids:
                    self.institutionids = Institution.objects.values_list(
                        'id', flat=True).filter(Q(boundary_id=boundaryid) |
                                                Q(boundary__parent_id=boundaryid) |
                                                Q(boundary__parent__parent_id=boundaryid))
            for institutionid in self.institutionids:
                for studentgroup in self.studentgroups:
                    studentgroupids = list(StudentGroup.objects.values_list(
                        'id', flat=True).filter(institution_id=institutionid, name=studentgroup))
                    if len(studentgroupids) != 0:
                        for studentgroupid in studentgroupids:
                            request.append({'assessment': assessmentid,
                                            'student_group': studentgroupid,
                                            'active': 2})

        serializer = self.get_serializer(data=request, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)


class AssessmentInstitutionAssociationViewSet(viewsets.ModelViewSet):
    assessmentids = []
    institutionids = []
    boundaryids = []
    queryset = AssessmentInstitutionAssociation.objects.all()
    serializer_class = AssessmentInstitutionAssociationSerializer

    def create(self, request, *args, **kwargs):
        if not self.request.data.get('assessmentid'):
            raise ParseError("Mandatory parameter assessmentid not passed")
        self.assessmentids = self.request.data.get('assessmentid').split(",")
        if self.request.data.get('boundaryid'):
            self.boundaryids = self.request.data.get('boundaryid').split(",")
        if self.request.data.get('institutionid'):
            self.institutionids = self.request.data.get('institutionid').split(",")
        if self.institutionids == [] and self.boundaryids == []:
            raise ParseError("Mandatory parameter institution or boundary not passed")
        response = self.createAssessmentInstitutionAssociation()

        return response

    def createAssessmentInstitutionAssociation(self):
        request = []
        for assessmentid in self.assessmentids:
            if self.institutionids == []:
                for boundaryid in self.boundaryids:
                    self.institutionids = Institution.objects.values_list(
                        'id', flat=True).filter(Q(boundary_id=boundaryid) |
                                                Q(boundary__parent_id=boundaryid) |
                                                Q(boundary__parent__parent_id=boundaryid))
            for institutionid in self.institutionids:
                request.append({'assessment': assessmentid,
                                'institution': institutionid,
                                'active': 2})
        serializer = self.get_serializer(data=request, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)
