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

-- schools_staff_type
ALTER TABLE ems_schools_staff_type RENAME TO schools_stafftype;

-- schools_academic_year
ALTER TABLE ems_schools_academic_year RENAME TO schools_academicyear;
ALTER TABLE schools_academicyear ADD start_year smallint; 
ALTER TABLE schools_academicyear ADD end_year smallint;
update schools_academic_year set start_year = (LEFT(name,4))::int2
update schools_academic_year set end_year = (RIGHT(name,4))::int2;

-- Step 2: Split the programme / assessment hierarchy

-- schools_answer
-- schools_assessments
-- schools_question
-- schools_programme

-- Step 3: Merge child and student tables See issue#19
-- schools_student
-- schools_child
-- schools_relations

-- Step 4: Merge Institution and Institution address tables  
-- schools_institution
-- schools_institution_address

-- Step 5: Import and Update Staff tables 
-- schools_staff
-- schools_staff_qualification

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
