-- This file contains all the transformation necessary to migrate the schema and
-- data from the old ems schema into the new ems schema  

-- Step 1 : Just rename the table which are not changing
-- These are tables which are enumeration foreign-key tables

-- schools_boundary_category
ALTER TABLE ems_schools_boundary_category RENAME TO schools_boundarycategory;

-- schools_boundary_type
ALTER TABLE ems_schools_boundary_type RENAME TO schools_boundarytype;

-- schools_boundary
ALTER TABLE ems_schools_boundary RENAME TO schools_boundary;

-- schools_moi_type
ALTER TABLE ems_schools_moi_type RENAME TO schools_moitype;

-- schools_institution_management
ALTER TABLE ems_schools_institution_management RENAME TO schools_institutionmanagement; 

-- schools_institution_category
ALTER TABLE ems_schools_institution_category RENAME TO schools_institutioncategory; 

-- schools_staff_qualifications
ALTER TABLE ems_schools_staff_qualifications RENAME TO schools_qualificationslist;

-- schools_staff_qualification
ALTER TABLE ems_schools_staff_qualification RENAME TO schools_staff_qualification;

-- schools_staff_type
ALTER TABLE ems_schools_staff_type RENAME TO schools_stafftype;

-- schools_academic_year
ALTER TABLE ems_schools_academic_year RENAME TO schools_academicyear;
ALTER TABLE schools_academicyear ADD start_year smallint; 
ALTER TABLE schools_academicyear ADD end_year smallint;
update schools_academic_year set start_year = (LEFT(name,4))::int2
update schools_academic_year set end_year = (RIGHT(name,4))::int2;

-- Step 2: Split the programme / assessment hierarchy

-- schools_programme
-- Split into schools_programmeinstitution and schools_programmestudent based on programme typ
-- Join with assessments table is necessary as type of programme cannot be determined without looking at associated assessments 
INSERT INTO schools_programmeinstitution SELECT a.id, a.name, a.description, a.start_date, a.end_date, a.active, a.programme_institution_category_id
FROM ems_schools_programme a
INNER JOIN ems_schools_assessment b
ON a.id = b.programme_id WHERE b.typ = 1 GROUP BY a.id, a.name, a.description, a.start_date, a.end_date, a.active, a.programme_institution_category_id;

INSERT INTO schools_programmestudent SELECT a.id, a.name, a.description, a.start_date, a.end_date, a.active, a.programme_institution_category_id
FROM ems_schools_programme a
INNER JOIN ems_schools_assessment b
ON a.id = b.programme_id WHERE b.typ = 3 GROUP BY a.id, a.name, a.description, a.start_date, a.end_date, a.active, a.programme_institution_category_id;

-- schools_assessments
-- Split into schools_assessmentinstitution and schools_assessmentstudent based on assessment typ
INSERT INTO schools_assessmentinstitution SELECT id, name, start_date, end_date, query, active, double_entry, flexi_assessment, primary_field_name,  primary_field_type,  programme_id FROM ems_schools_assessment WHERE typ = 3;
INSERT INTO schools_assessmentstudent SELECT id, name, start_date, end_date, query, active, double_entry, flexi_assessment, primary_field_name,  primary_field_type,  programme_id FROM ems_schools_assessment WHERE typ = 1;

-- schools_answer
-- content_type_id for student is 24 and content_type_id for institution is 18
INSERT INTO schools_answerstudent select id, answer_score, answer_grade, double_entry, status, creation_date, last_modified_date, flexi_data, last_modified_by_id, question_id, user1_id, user2_id from ems_schools_answer where content_type_id = 24;

INSERT INTO schools_answerinstitution select id, answer_score, answer_grade, double_entry, status, creation_date, last_modified_date, flexi_data, last_modified_by_id, question_id, user1_id, user2_id from ems_schools_answer where content_type_id = 18;

-- schools_question
-- Separate questions based on assessment.typ
INSERT INTO schools_questioninstitution SELECT a.id, a.name, a.question_type, a.score_min, a.score_max, a.grade, a.order, a.double_entry, a.active, a.assessment_id
FROM ems_schools_question a
INNER JOIN ems_schools_assessment b
ON a.assessment_id = b.id WHERE b.typ = 1;

INSERT INTO schools_questionstudent SELECT a.id, a.name, a.question_type, a.score_min, a.score_max, a.grade, a.order, a.double_entry, a.active, a.assessment_id
FROM ems_schools_question a
INNER JOIN ems_schools_assessment b
ON a.assessment_id = b.id WHERE b.typ = 3;


-- Step 3: Merge child and student tables See issue#19
-- schools_relations
-- replace child_id with student_id 
INSERT INTO schools_relations SELECT a.id, a.relation_type, a.first_name, a.middle_name, a.last_name, b.id
FROM ems_schools_relations a 
INNER JOIN ems_schools_student b 
ON a.child_id = b.child_id;

-- schools_student
INSERT INTO schools_student SELECT a.id, a.active, b.dob, b.first_name, b.gender, b.last_name, b.middle_name, b.mt_id, b.uid
FROM ems_schools_student a
INNER JOIN ems_schools_child b
on a.child_id = b.id;

-- schools_child
-- drop this table later

-- Step 4: Merge Institution and Institution address tables  
-- schools_institution
-- merge the institution address with this table

INSERT INTO schools_institution SELECT a.id, a.dise_code, a.name, a.institution_gender, a.active, a.boundary_id, a.cat_id, a.mgmt_id, b.address, b.area, b.instidentification, b.instidentification2, b.landmark, b.pincode, b.route_information 
FROM ems_schools_institution a 
INNER JOIN ems_schools_institution_address b 
ON a.inst_address_id = b.id;
 
-- schools_institution_address
-- drop this table later

-- Step 5: Import and Update Staff tables 
-- schools_staff
-- reorder fields and remove uid column
INSERT INTO schools_staff SELECT id, first_name, middle_name, last_name, doj, gender, active, institution, mt_id, staff_type_id FROM ems_schools_staff;

-- Step 6: Update other tables
-- schools_assessment_class_association
-- schools_assessment_institution_association
-- schools_assessment_studentgroup_association
-- schools_institution_languages
-- schools_staff_studentgrouprelation
-- schools_student_studentgrouprelation
-- schools_studentgroup

-- FIXME : Add List of id sequences
-- FIXME : Add indices for specific tables
-- FIXME : Drop ems_* tables after migration is done
