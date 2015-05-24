-- schools_academic_year
ALTER TABLE ems_schools_academic_year TO schools_academic_year;
ALTER TABLE schools_academic_year ADD start_year smallint; 
ALTER TABLE schools_academic_year ADD end_year smallint;
update schools_academic_year set start_year = (LEFT(name,4))::int2
update schools_academic_year set end_year = (RIGHT(name,4))::int2;

-- schools_answer
-- schools_assessments
-- schools_assessment_class_association
-- schools_assessment_institution_association
-- schools_assessment_lookup
-- schools_assessment_studentgroup_association
-- schools_boundary
-- schools_boundary_category
-- schools_boundary_type
-- schools_child
-- schools_institution
-- schools_institution_address
-- schools_institution_category
-- schools_institution_languages
-- schools_institution_management
-- schools_moi_type
-- schools_programme
-- schools_question
-- schools_relations
-- schools_staff
-- schools_staff_qualification
-- schools_staff_qualifications
-- schools_staff_studentgrouprelation
-- schools_staff_type
-- schools_student
-- schools_student_studentgrouprelation
-- schools_studentgroup
-- schools_taggeditem
-- schools_userassessmentpermissions

-- FIXME : Add List of id sequences
-- FIXME : Add indices for specific tables
