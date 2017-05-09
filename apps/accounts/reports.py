import ast
from itertools import chain
from easyaudit.models import CRUDEvent
from guardian.shortcuts import (
    assign_perm,
    get_objects_for_user,
    remove_perm
)

from django.contrib.contenttypes.models import ContentType

from schools.models import (
    Assessment,
    AnswerInstitution,
    AnswerStudent,
    AnswerStudentGroup,
    Boundary,
    BoundaryCategory,
    BoundaryType,
    Institution,
    Staff,
    Student,
    StudentGroup,
)

ASSESSMENT_TYPE = {
    1 : 'Institution',
    2 : 'Student Group',
    3 : 'Student'
}

class Report(object):
    def __init__(self, user, from_date, to_date):
        self.user = user
        self.from_date = from_date
        self.to_date = to_date

    def fetch_user_answers_for_assessment(self, questions, answer_ids_by_user):
        institution_answers = AnswerInstitution.objects.filter(
            id__in=answer_ids_by_user,
            question__in=questions
        )
        student_answers = AnswerStudent.objects.filter(
            id__in=answer_ids_by_user,
            question__in=questions
        )
        studentgroup_answers = AnswerStudentGroup.objects.filter(
            id__in=answer_ids_by_user,
            question__in=questions
        )
        answers = list(chain(institution_answers, student_answers, studentgroup_answers))
        return answers

    def get_content_types(self, models=None):
        app = 'schools'
        if models:
            models = models
        else:
            models = [
                'student', 'institution', 'staff', 'answerinstitution',
                'answerstudent', 'answerstudentgroup'
            ]
        return [ContentType.objects.get(app_label=app, model=model) for model in models]

    def get_instances_count(self, crud_events, instance_ids, instance_type):
        return (
            crud_events.filter(
                object_id__in=instance_ids,
                content_type=instance_type,
                event_type=CRUDEvent.CREATE
            ).count(),
            crud_events.filter(
                object_id__in=instance_ids,
                content_type=instance_type,
                event_type=CRUDEvent.UPDATE
            ).count(),
            crud_events.filter(
                object_id__in=instance_ids,
                content_type=instance_type,
                event_type=CRUDEvent.DELETE
            ).count()
        )

    def get_correct_and_incorrects(self, report_dict, questions, crud_events):
        answers_ctypes = self.get_content_types(
            models=['answerinstitution', 'answerstudent', 'answerstudentgroup']
        )
        answer_ids_created_by_user = crud_events.filter(
            content_type__in=answers_ctypes,
            event_type=CRUDEvent.CREATE
        ).values_list('object_id', flat=True)
        answers = self.fetch_user_answers_for_assessment(
            questions, answer_ids_created_by_user)

        for answer in answers:
            try:
                updated_answer = CRUDEvent.objects.get(
                    object_id=answer.id,
                    event_type=CRUDEvent.UPDATE
                )
            except:
                # Double entry not done.
                continue

            updated_answer = self.get_answer_json(updated_answer)
            
            # If question type is Marks
            if answer.question.question_type == 1:
                if int(answer.answer_score) == int(updated_answer['fields']['answer_score']):
                    report_dict['Correct'] += 1
                else:
                    report_dict['Incorrect'] += 1
            else: # If question type is Grade
                if answer.answer_grade == updated_answer['fields']['answer_grade']:
                    report_dict['Correct'] += 1
                else:
                    report_dict['Incorrect'] += 1

        return report_dict

    def get_verified_and_rectifieds(self, report_dict, questions, crud_events):
        answers_ctypes = self.get_content_types(
            models=['answerinstitution', 'answerstudent', 'answerstudentgroup']
        )
        answer_ids_updated_by_user = crud_events.filter(
            content_type__in=answers_ctypes,
            event_type=CRUDEvent.UPDATE
        ).values_list('object_id', flat=True)

        answers = self.fetch_user_answers_for_assessment(
            questions, answer_ids_updated_by_user)

        for answer in answers:
            original_answer = CRUDEvent.objects.get(
                object_id=answer.id,
                event_type=CRUDEvent.CREATE
            )

            original_answer = self.get_answer_json(original_answer)
            
            # If question type is Marks
            if answer.question.question_type == 1:
                if int(answer.answer_score) == int(original_answer['fields']['answer_score']):
                    report_dict['Verified'] += 1
                else:
                    report_dict['Rectified'] += 1
            else: # If question type is Grade
                if answer.answer_grade == original_answer['fields']['answer_grade']:
                    report_dict['Verified'] += 1
                else:
                    report_dict['Rectified'] += 1

        return report_dict

    def get_answer_json(self, answer):
        # This is a small hack since the json representation
        # of the object is stored as string. We first replace
        # all occurences of 'null' with 'None' and then use
        # literal_eval to convert it into a Python object.
        # Since the structue is like '[{...}]', it is a list.
        # Hence we add the [0] to the end to get the first
        # object which is the JSON.
        return ast.literal_eval(
            answer.object_json_repr.replace('null', 'None')
        )[0]

    def generate(self):
        user = self.user
        
        report_dict = {
            'Correct':0,
            'Incorrect':0,
            'Verified':0,
            'Rectified':0,
        }
        response = {}

        crud_events = CRUDEvent.objects.filter(user=user)

        from_date = self.from_date
        to_date = self.to_date

        if from_date:
            crud_events = crud_events.filter(datetime__gte=from_date)

        if to_date:
            crud_events = crud_events.filter(datetime__lte=to_date)

        # Get all the related ContentTypes.
        (ctype_student, ctype_institution, ctype_staff, ctype_answer_institution,
         ctype_answer_student, ctype_answer_studentgroup) = self.get_content_types()

        ## Get all the primary and pre school records.

        # Boundaries
        primary_school_boundary = BoundaryType.objects.get(name="Primary School")
        pre_school_boundary = BoundaryType.objects.get(name="PreSchool")

        # Schools
        primary_schools = Institution.objects.filter(
            boundary__boundary_type=primary_school_boundary)
        pre_schools = Institution.objects.filter(
            boundary__boundary_type=pre_school_boundary)

        # Studentgroups
        primary_school_studentrgoups = StudentGroup.objects.filter(
            institution__in=primary_schools)
        pre_school_studentrgoups = StudentGroup.objects.filter(
            institution__in=pre_schools)

        # Students
        primary_school_students = Student.objects.filter(
            studentstudentgrouprelation__student_group__in=primary_school_studentrgoups)

        pre_school_students = Student.objects.filter(
            studentstudentgrouprelation__student_group__in=pre_school_studentrgoups)

        # Staffs
        primary_school_staffs = Staff.objects.filter(
            institution__in=primary_schools)

        pre_school_staffs = Staff.objects.filter(
            institution__in=pre_schools)

        ## Get the aggregates.

        # Primary School aggregates
        (primary_students_created,
         primary_students_updated,
         primary_students_deleted) = self.get_instances_count(
             crud_events, primary_school_students, ctype_student)
        
        (primary_institutions_created,
         primary_institutions_updated,
         primary_institutions_deleted) = self.get_instances_count(
            crud_events, primary_schools, ctype_institution)
         
        (primary_staffs_created,
         primary_staffs_updated,
         primary_staffs_deleted) = self.get_instances_count(
            crud_events, primary_school_staffs, ctype_staff)

        # Pre School aggregates
        (pre_students_created,
         pre_students_updated,
         pre_students_deleted) = self.get_instances_count(
            crud_events, pre_school_students, ctype_student)
         
        (pre_institutions_created,
         pre_institutions_updated,
         pre_institutions_deleted) = self.get_instances_count(
            crud_events, pre_schools, ctype_institution)
         
        (pre_staffs_created,
         pre_staffs_updated,
         pre_staffs_deleted) = self.get_instances_count(
            crud_events, pre_school_staffs, ctype_staff)

        authorized_assessment_ids = get_objects_for_user(
            user, "crud_answers", klass=Assessment
        ).values_list('id', flat=True)

        for assessment in Assessment.objects.filter(id__in=authorized_assessment_ids):
            programme_name = assessment.programme.name.strip()
            programme_id = assessment.programme.id
            if not programme_name in response: 
                response[programme_name] = {
                    'id':programme_id,
                    'assessments':[]
                }
            questions = assessment.question_set.all()
            report_dict = self.get_correct_and_incorrects(
                report_dict, questions, crud_events
            )
            report_dict = self.get_verified_and_rectifieds(
                report_dict, questions, crud_events
            )

            assessment_dict = {
                'id':assessment.id,
                'name':assessment.name,
                'type':ASSESSMENT_TYPE[assessment.type],
                'number_of_questions':questions.count(),
                user.username:report_dict
            }

            response[assessment.programme.name.strip()]['assessments'].append(assessment_dict)

        response['preschool'] = {
            'students': {
                'created':pre_students_created,
                'updated':pre_students_updated,
                'deleted':pre_students_deleted,
            },
            'institutions': {
                'created':pre_institutions_created,
                'updated':pre_institutions_updated,
                'deleted':pre_institutions_deleted,
            },
            'staffs': {
                'created':pre_staffs_created,
                'updated':pre_staffs_updated,
                'deleted':pre_staffs_deleted,
            },
        }
        response['primaryschool'] = {
            'students': {
                'created':primary_students_created,
                'updated':primary_students_updated,
                'deleted':primary_students_deleted,
            },
            'institutions': {
                'created':primary_institutions_created,
                'updated':primary_institutions_updated,
                'deleted':primary_institutions_deleted,
            },
            'staffs': {
                'created':primary_staffs_created,
                'updated':primary_staffs_updated,
                'deleted':primary_staffs_deleted,
            },
        }

        return response
