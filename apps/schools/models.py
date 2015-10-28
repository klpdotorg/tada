#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
import datetime
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User

PRIMARY_FIELD_TYPE = [(0, 'Default'),(1, 'Integer'), (2, 'Char'), (3, 'Date'), (4,
                      'Lookup')]

ACTIVE_STATUS = [
    (0, 'Deleted'),
    (1, 'Inactive'),
    (2, 'Active'),
    (3, 'Promoted'),
    (4, 'Promotion Failed'),
    (5, 'Passed Out'),
    (6, 'Detained'),
    (7, 'Completed'),
    ]

INSTITUTION_GENDER = [('boys', 'boys'), ('girls', 'girls'), ('co-ed',
                      'co-ed')]

GENDER = [('male', 'male'), ('female', 'female')]

GROUP_TYPE = [('Class', 'Class'), ('Center', 'Center')]

QUESTION_TYPE = [(1, 'Marks'), (2, 'Grade')]

RELATION_TYPE = [('Mother', 'Mother'), ('Father', 'Father'), ('Siblings'
                 , 'Siblings')]

ASSESSMENT_TYPE = [(1, 'Institution'), (2, 'Student Group'), (3,
                   'Student')]

Alpha_list = [('', 'No Section')]
for typ in range(ord('a'), ord('z') + 1):
    alph = chr(typ).upper()
    typs = (alph, alph)
    Alpha_list.append(typs)


class InstitutionCategory(models.Model):
    '''This Class stores the Institution Category Information'''

    name = models.CharField(max_length=50)
    category_type = models.IntegerField()

    def __unicode__(self):
        return '%s' % self.name


class MoiType(models.Model):
    '''This Class stores the Mother Toungue (Languages) Information'''

    name = models.CharField(max_length=50)

    def __unicode__(self):
        return '%s' % self.name

class InstitutionManagement(models.Model):
    '''This Class stores the Institution Management Information'''

    name = models.CharField(max_length=50)

    def __unicode__(self):
        return '%s' % self.name

class BoundaryCategory(models.Model):
    '''This Class stores the Boundary Category Information'''

    boundary_category = models.CharField(max_length=100)

    def __unicode__(self):
        return '%s' % self.boundary_category

class BoundaryType(models.Model):
    '''This Class stores the Boundary Type Information'''

    boundary_type = models.CharField(max_length=100)

    def __unicode__(self):
        return '%s' % self.boundary_type

class StaffType(models.Model):
    '''This Class stores information about Staff Type'''

    staff_type = models.CharField(max_length=100)
    category_type = models.IntegerField()

    def __unicode__(self):
        return '%s' % self.staff_type


class QualificationList(models.Model):
    ''' This Class Stores Information about staff qualification '''

    qualification = models.CharField(max_length=100)

    def __unicode__(self):
        return '%s' % self.qualification

class CompensationAuditLog(models.Model):
    ''' This class stores information about additions or deletion to entitities in EMS '''

    user = models.CharField(max_length=100)
    audit_time = models.DateField(max_length=20, default=datetime.date.today)
    entity_name = models.CharField(max_length=100)
    operation_type = models.CharField(max_length=20)
    operation_value = models.CharField(max_length=20)

    def __unicode__(self):
        return '%s' % self.user

class Boundary(models.Model):
    '''This class specifies the longitude and latitute of the area'''

    parent = models.ForeignKey('self', blank=True, null=True)
    name = models.CharField(max_length=300)
    boundary_category = models.ForeignKey(BoundaryCategory,
            blank=True, null=True)
    boundary_type = models.ForeignKey(BoundaryType, blank=True,
            null=True)
    active = models.IntegerField(blank=True, null=True, default=2)

    class Meta:
        """ Used For ordering """

        ordering = ['name']

    def __unicode__(self):
        return '%s' % self.name

    def getChild(self, boundaryType):
        if Boundary.objects.filter(parent__id=self.id, active=2,
                                   boundary_type=boundaryType).count():
            return True
        elif Institution.objects.filter(boundary__id=self.id,
                active=2).count():
            return True
        else:
            return False

    def getModuleName(self):
        return 'boundary'

    def get_view_url(self, boundaryType):
        return '/boundary/%s/%s/view/' % (self.id, boundaryType)

    def get_edit_url(self):
        return '/boundary/%s/update/' % self.id

    def get_update_url(self):
        return '/boundary/%d/update/' % self.id

    def getPermissionChild(self, boundaryType):
        if Boundary.objects.filter(parent__id=self.id, active=2,
                                   boundary_type=boundaryType):
            return True
        else:
            return False

class Institution(models.Model):
    ''' It stores the all data regarding Institutions'''

    boundary = models.ForeignKey(Boundary)
    dise_code = models.CharField(max_length=14, blank=True, null=True)
    name = models.CharField(max_length=300)
    cat = models.ForeignKey(InstitutionCategory, blank=True, null=True)
    institution_gender = models.CharField(max_length=10,
            choices=INSTITUTION_GENDER, default='co-ed')
    languages = models.ManyToManyField(MoiType)
    mgmt = models.ForeignKey(InstitutionManagement, default='1')
    address = models.CharField(max_length=1000,default='NA')
    area = models.CharField(max_length=200, blank=True, null=True)
    pincode = models.CharField(max_length=100, blank=True, null=True)
    landmark = models.CharField(max_length=1000, blank=True, null=True,
                                help_text='Can be comma separated')
    instidentification = models.CharField(max_length=1000, blank=True,
            null=True, help_text='Can be comma separated')
    instidentification2 = models.CharField(max_length=1000, blank=True,
            null=True, help_text='Can be comma separated')
    route_information = models.CharField(max_length=500, blank=True,
            null=True, help_text='Can be comma separated')
    active = models.IntegerField(blank=True, null=True, default=2)

    class Meta:

        ordering = ['name']

    def __unicode__(self):
        return '%s' % self.name

    def get_all_cat(self, category_type):
        return InstitutionCategory.objects.all(category_type=category_type)

    def getChild(self):
        if StudentGroup.objects.filter(institution__id=self.id,
                active=2).count():
            return True
        else:
            return False

    def get_all_mgmt(self):
        return institution_Management.objects.all()

    def get_all_languages(self):
        return MoiType.objects.all()

    def getModuleName(self):
        return 'institution'

    def get_update_url(self):
        return '/institution/%d/update/' % self.id

    def get_view_url(self):
        return '/institution/%s/view/' % self.id

    def get_edit_url(self):
        return '/institution/%s/update/' % self.id

    def save(self, *args, **kwargs):
        # custom save method
        #pdb.set_trace()
        from django.db import connection
        connection.features.can_return_id_from_insert = False
        #print "save"

        #print "name is",self.name, "=================== active is", self.active
        self.full_clean()
        super(Institution, self).save(*args, **kwargs)

from django.db.models.signals import post_save, pre_save


class Relations(models.Model):
    ''' This class stores relation information of the childrens'''

    relation_type = models.CharField(max_length=10,
            choices=RELATION_TYPE, default='Mother')
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    student = models.ForeignKey("Student")

    def __unicode__(self):
        return '%s' % self.first_name

    def get_view_url(self):
        return ''


class StudentGroup(models.Model):
    ''' Here it holds the informaion of the class and section of the Institutions'''

    institution = models.ForeignKey(Institution)
    name = models.CharField(max_length=50)
    section = models.CharField(max_length=10, choices=Alpha_list,
                               blank=True, default='')
    active = models.IntegerField(blank=True, null=True, default=2)
    group_type = models.CharField(max_length=10, choices=GROUP_TYPE,
                                  default='Class')

    class Meta:

        unique_together = (('institution', 'name', 'section'), )
        ordering = ['name', 'section']

    def __unicode__(self):
        return '%s' % self.name

    def getChild(self):
        return False

    def getSchoolIdentity(self):
        return '%s: %s' % (self.institution__id, self.institution__name)

    def getModuleName(self):
        return 'studentgroup'

    def get_update_url(self):
        return '/studentgroup/%d/update/' % self.id

    def get_view_url(self):
        return '/studentgroup/%s/view/' % self.id

    def save(self, *args, **kwargs):
        # custom save method
        #pdb.set_trace()
        from django.db import connection
        connection.features.can_return_id_from_insert = False
        #print "save"

        #print "name is",self.name, "=================== active is", self.active
        self.full_clean()
        super(StudentGroup, self).save(*args, **kwargs)

class AcademicYear(models.Model):
    ''' Its stores the academic years information'''

    name = models.CharField(max_length=20, unique=True)
    active = models.IntegerField(blank=True, null=True, default=0)
    start_year = models.IntegerField(blank=True, null=False, default=0)
    end_year = models.IntegerField(blank=True, null=False,default=0)
    def __unicode__(self):
        return self.name

def current_academic():
    ''' To select current academic year'''
    try:
        academicObj = AcademicYear.objects.get(active=1)
        return academicObj
    except AcademicYear.DoesNotExist:
        return 1

def default_end_date():
    ''' To select academic year end date'''

    now = datetime.date.today()
    currentYear = int(now.strftime('%Y'))
    currentMont = int(now.strftime('%m'))
    academicYear = current_academic().name
    academicYear = academicYear.split('-')
    if currentMont > 5 and int(academicYear[0]) == currentYear:
        academic_end_date = datetime.date(currentYear+1,12, 30)
    else:
        academic_end_date = datetime.date(currentYear, 5, 30)
    return academic_end_date

class Staff(models.Model):
    '''This Class stores the Institution Worker(Staff) Information'''

    institution = models.ForeignKey(Institution, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    doj = models.DateField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER,
                              default='female')
    mt = models.ForeignKey(MoiType, default=1)

    qualification = models.ManyToManyField(QualificationList,
            blank=True)
    staff_type = models.ForeignKey(StaffType, default=1)
    active = models.IntegerField(blank=True, null=True, default=2)

    class Meta:

        ordering = ['first_name', 'middle_name', 'last_name']

    def __unicode__(self):
        return '%s %s %s' % (self.first_name, self.middle_name,
                             self.last_name)

    def getAssigendClasses(self):
        return StudentGroup.objects.filter(staff_studentgrouprelation__staff__id=self.id,
                staff_studentgrouprelation__active=2)


class Student(models.Model):
    ''' This class gives information regarding the students class , academic year and personnel details'''

    first_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    uid = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(max_length=20,null=True)
    gender = models.CharField(max_length=10, choices=GENDER,
                              default='male')
    mt = models.ForeignKey(MoiType, default='1')
    active = models.IntegerField(blank=True, null=True, default=2)
    
    class Meta:

        ordering = ['first_name', 'middle_name', 'last_name']
    
    def __unicode__(self):
        return '%s' % self.first_name

    def getMother(self):
        return Relations.objects.get(relation_type='Mother',
                child__id=self.id)

    def getStudent(self):
        return Student.objects.get(child__id=self.id)


    def GetName(self):
        return self.child.first_name

    def getChild(self):
        return False

    def get_all_academic_years(self):
        return AcademicYear.objects.all()

    def get_all_languages(self):
        return MoiType.objects.all()

    def getModuleName(self):
        return 'student'

    def save(self, *args, **kwargs):
        # custom save method
        #pdb.set_trace()
        from django.db import connection
        connection.features.can_return_id_from_insert = False
        #print "save"

        #print "active is", self.active
        self.full_clean()
        super(Student, self).save(*args, **kwargs)

class StudentStudentGroupRelation(models.Model):
    '''This Class stores the Student and Student Group Relation Information'''

    student = models.ForeignKey(Student)
    student_group = models.ForeignKey(StudentGroup)
    academic = models.ForeignKey(AcademicYear,
                                 default=current_academic)
    active = models.IntegerField(blank=True, null=True, default=2)

    class Meta:

        unique_together = (('student', 'student_group', 'academic'), )

    def save(self, *args, **kwargs):
        # custom save method
        #pdb.set_trace()
        from django.db import connection
        connection.features.can_return_id_from_insert = False
        #print "save"

        #print "active is", self.active
        self.full_clean()
        super(Student_StudentGroupRelation, self).save(*args, **kwargs)

class StaffStudentGroupRelation(models.Model):
    '''This Class stores the Staff and Student Group Relation Information'''

    staff = models.ForeignKey(Staff)
    student_group = models.ForeignKey(StudentGroup)
    academic = models.ForeignKey(AcademicYear,
                                 default=current_academic)
    active = models.IntegerField(blank=True, null=True, default=2)

    class Meta:

        unique_together = (('staff', 'student_group', 'academic'), )


class ProgrammeInstitution(models.Model):
    """ This class Stores information about Programme """

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True,
                                   null=True)
    start_date = models.DateField(max_length=20,
                                 default=datetime.date.today)
    end_date = models.DateField(max_length=20, default=default_end_date)
    programme_institution_category = models.ForeignKey(BoundaryType,
            blank=True, null=True)
    active = models.IntegerField(blank=True, null=True, default=2)

    class Meta:

        ordering = ['-start_date', '-end_date', 'name']

    def __unicode__(self):
        return '%s (%s-%s)' % (self.name, self.start_date.strftime('%Y'
                               ), self.end_date.strftime('%Y'))

    def get_view_url(self):
        return '/programme/%s/view/' % self.id

    def get_edit_url(self):
        return '/programme/%s/update/' % self.id

    def getModuleName(self):
        return 'programmeInstitution'


class ProgrammeStudent(models.Model):
    """ This class Stores information about Programme """

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True,
                                   null=True)
    start_date = models.DateField(max_length=20,
                                 default=datetime.date.today)
    end_date = models.DateField(max_length=20, default=default_end_date)
    programme_institution_category = models.ForeignKey(BoundaryType,
            blank=True, null=True)
    active = models.IntegerField(blank=True, null=True, default=2)

    class Meta:

        ordering = ['-start_date', '-end_date', 'name']

    def __unicode__(self):
        return '%s (%s-%s)' % (self.name, self.start_date.strftime('%Y'
                               ), self.end_date.strftime('%Y'))

    def get_view_url(self):
        return '/programme/%s/view/' % self.id

    def get_edit_url(self):
        return '/programme/%s/update/' % self.id

    def getModuleName(self):
        return 'programmeStudent'




class AssessmentInstitution(models.Model):
    """ This class stores information about Assessment """

    programme = models.ForeignKey(ProgrammeInstitution)
    name = models.CharField(max_length=100)
    start_date = models.DateField(max_length=20,
                                 default=datetime.date.today)
    end_date = models.DateField(max_length=20, default=default_end_date)
    query = models.CharField(max_length=500, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True, default=2)
    double_entry = models.BooleanField('Requires double entry',
            default=True)
    flexi_assessment = \
        models.BooleanField('Allows multiple sets of answer per assessment'
                            , default=False)
    primary_field_name = models.CharField(max_length=500, blank=True,
            null=True)
    PRIMARY_FIELD_TYPE = \
        models.IntegerField(choices=PRIMARY_FIELD_TYPE, default=3,
                            null=True)

    class Meta:

        unique_together = (('programme', 'name'), )
        ordering = ['start_date']

    def __unicode__(self):
        return '%s' % self.name

    def get_view_url(self):
        return '/assessment/%s/view/' % self.id

    def get_edit_url(self):
        return '/assessment/%s/update/' % self.id

    def getChild(self):
        if Question.objects.filter(assessment__id=self.id,
                                   active=2).count():
            return True
        else:
            return False

    def getModuleName(self):
        return 'assessmentInstitution'

class AssessmentStudent(models.Model):
    """ This class stores information about Assessment """

    programme = models.ForeignKey(ProgrammeStudent)
    name = models.CharField(max_length=100)
    start_date = models.DateField(max_length=20,
                                 default=datetime.date.today)
    end_date = models.DateField(max_length=20, default=default_end_date)
    query = models.CharField(max_length=500, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True, default=2)
    double_entry = models.BooleanField('Requires double entry',
            default=True)
    flexi_assessment = \
        models.BooleanField('Allows multiple sets of answer per assessment'
                            , default=False)
    primary_field_name = models.CharField(max_length=500, blank=True,
            null=True)
    PRIMARY_FIELD_TYPE = \
        models.IntegerField(choices=PRIMARY_FIELD_TYPE, default=3,
                            null=True)

    class Meta:

        unique_together = (('programme', 'name'), )
        ordering = ['start_date']

    def __unicode__(self):
        return '%s' % self.name

    def get_view_url(self):
        return '/assessment/%s/view/' % self.id

    def get_edit_url(self):
        return '/assessment/%s/update/' % self.id

    def getChild(self):
        if Question.objects.filter(assessment__id=self.id,
                                   active=2).count():
            return True
        else:
            return False

    def getModuleName(self):
        return 'assessmentStudent'

class AssessmentStudentGroupAssociation(models.Model):
    '''This Class stores the Assessment and Student Group Association Information'''

    assessment = models.ForeignKey(AssessmentStudent)
    student_group = models.ForeignKey(StudentGroup)
    active = models.IntegerField(blank=True, null=True, default=2)


    def save(self, *args, **kwargs):
        # custom save method
        #pdb.set_trace()
        from django.db import connection
        connection.features.can_return_id_from_insert = False
        #print "save"

        #print "Access", self.active
        self.full_clean()
        super(Assessment_StudentGroup_Association, self).save(*args, **kwargs)

    class Meta:

        unique_together = (('assessment', 'student_group'), )

class AssessmentInstitutionAssociation(models.Model):
    '''This Class stores the Assessment and Student Group Association Information'''

    assessment = models.ForeignKey(AssessmentStudent)
    institution = models.ForeignKey(Institution)
    active = models.IntegerField(blank=True, null=True, default=2)

    class Meta:

        unique_together = (('assessment', 'institution'), )


class QuestionStudent(models.Model):
    """ This class stores Assessment detail information """

    assessment = models.ForeignKey(AssessmentStudent)
    name = models.CharField(max_length=200)
    question_type = models.IntegerField(choices=QUESTION_TYPE, default=1)
    score_min = models.DecimalField(max_digits=10, decimal_places=2,
                                   blank=True, null=True)
    score_max = models.DecimalField(max_digits=10, decimal_places=2,
                                   blank=True, null=True)
    grade = models.CharField(max_length=100, blank=True, null=True)
    order = models.IntegerField()
    double_entry = models.BooleanField(default=True)
    active = models.IntegerField(blank=True, null=True, default=2)

    class Meta:

        unique_together = (('assessment', 'name'), )
        ordering = ['order']

    def __unicode__(self):
        return self.name

    def getAllGrades(self):
        return gradeList

    def getSelectedGrades(self):
        if self.grade:
            return self.grade.split(',')
        else:
            return ''

    def getChild(self):
        return False

    def getModuleName(self):
        return 'questionStudent'

    def get_view_url(self):
        return '/question/%s/view/' % self.id

    def get_edit_url(self):
        return '/question/%s/update/' % self.id


class QuestionInstitution(models.Model):
    """ This class stores Assessment detail information """

    assessment = models.ForeignKey(AssessmentInstitution)
    name = models.CharField(max_length=200)
    question_type = models.IntegerField(choices=QUESTION_TYPE, default=1)
    score_min = models.DecimalField(max_digits=10, decimal_places=2,
                                   blank=True, null=True)
    score_max = models.DecimalField(max_digits=10, decimal_places=2,
                                   blank=True, null=True)
    grade = models.CharField(max_length=100, blank=True, null=True)
    order = models.IntegerField()
    double_entry = models.BooleanField(default=True)
    active = models.IntegerField(blank=True, null=True, default=2)

    class Meta:

        unique_together = (('assessment', 'name'), )
        ordering = ['order']

    def __unicode__(self):
        return self.name

    def getAllGrades(self):
        return gradeList

    def getSelectedGrades(self):
        if self.grade:
            return self.grade.split(',')
        else:
            return ''

    def getChild(self):
        return False

    def getModuleName(self):
        return 'questionInstitution'

    def get_view_url(self):
        return '/question/%s/view/' % self.id

    def get_edit_url(self):
        return '/question/%s/update/' % self.id



class AnswerStudent(models.Model):
    """ This class stores information about student marks and grade """
    
    question = models.ForeignKey(QuestionStudent)

    # student = models.IntegerField(blank = True, null = True,default=0) # models.ForeignKey(Student)

    answer_score = models.DecimalField(max_digits=10, decimal_places=2,
            blank=True, null=True)
    answer_grade = models.CharField(max_length=30, blank=True, null=True)
    double_entry = models.IntegerField(blank=True, null=True, default=0)
    status = models.IntegerField(blank=True, null=True)
    user1 = models.ForeignKey(User, blank=True, null=True,
                              related_name='user1')
    user2 = models.ForeignKey(User, blank=True, null=True,
                              related_name='user2')
    creation_date = models.DateField(auto_now_add=True,
                                    blank=True, null=True)
    last_modified_date = models.DateField(auto_now=True,
            blank=True, null=True)
    last_modified_by = models.ForeignKey(User, blank=True, null=True,
            related_name='last_modified_answer_student')
    flexi_data = models.CharField(max_length=30, blank=True, null=True)

    class Meta:

        unique_together = (('question', 'flexi_data'), )


    def save(self, *args, **kwargs):
        # custom save method
        #pdb.set_trace()
        from django.db import connection
        connection.features.can_return_id_from_insert = False
        #print "save"

        #print "=================== status is", self.status
        self.full_clean()
        super(AnswerStudent, self).save(*args, **kwargs)

class AnswerInstitution(models.Model):
    """ This class stores information about student marks and grade """
    
    question = models.ForeignKey(QuestionInstitution)

    # student = models.IntegerField(blank = True, null = True,default=0) # models.ForeignKey(Student)

    answer_score = models.DecimalField(max_digits=10, decimal_places=2,
            blank=True, null=True)
    answer_grade = models.CharField(max_length=30, blank=True, null=True)
    double_entry = models.IntegerField(blank=True, null=True, default=0)
    status = models.IntegerField(blank=True, null=True)
    user1 = models.ForeignKey(User, blank=True, null=True,
                              related_name='user1_answer_institution')
    user2 = models.ForeignKey(User, blank=True, null=True,
                              related_name='user2_answer_institution')
    creation_date = models.DateField(auto_now_add=True,
                                    blank=True, null=True)
    last_modified_date = models.DateField(auto_now=True,
            blank=True, null=True)
    last_modified_by = models.ForeignKey(User, blank=True, null=True,
            related_name='last_modified_answer_institution')
    flexi_data = models.CharField(max_length=30, blank=True, null=True)

    class Meta:

        unique_together = (('question', 'flexi_data'), )


    def save(self, *args, **kwargs):
        # custom save method
        #pdb.set_trace()
        from django.db import connection
        connection.features.can_return_id_from_insert = False
        #print "save"

        #print "=================== status is", self.status
        self.full_clean()
        super(AnswerInstitution, self).save(*args, **kwargs)

def call(sender, method, instance):
    func = getattr(sender, method, None)
    if callable(func):
        func(instance)

def post_save_hook(sender, **kwargs):
    if kwargs['created']:
        call(sender, 'after_create', kwargs['instance'])
        if kwargs['instance'].boundary_type.id == 2:
            a=BoundaryCategory.objects.get(id=13)
            obj = Boundary.objects.get(id=kwargs['instance'].id)
            if obj.parent.id == 1:
                obj.boundary_category = a
                obj.save()
    else:
        call(sender, 'after_update', kwargs['instance'])
    call(sender, 'after_save', kwargs['instance'])

post_save.connect(post_save_hook, sender=Boundary)
