from os import system
import os

#Before running this script 

#change this to point to the ems database that is used.
database="emstemp"
if not os.path.exists("load"):
    os.makedirs("load")
inputdatafile="getdata.sql"
inputfile=open(inputdatafile,'w',0)
loaddatafile="loaddata.sql"
loadfile=open(loaddatafile,'w',0)
command="psql -U klp -d "+database+" -f cleanems.sql"
system(command)

tables=[
{ 'schools_academicyear':"copy (select id,name,active,(LEFT(name,4))::int2,(RIGHT(name,4))::int2 from schools_academic_year) to '$PWD/load/schools_academicyear.csv' NULL 'null' DELIMITER ',' quote '\\\"' csv;" },
{'schools_boundarycategory':"copy (select * from schools_boundary_category) to '$PWD/load/schools_boundarycategory.csv' NULL 'null' DELIMITER ',' quote '\\\"' csv;"}, 
{'schools_boundarytype':"COPY schools_boundary_type TO '$PWD/load/schools_boundarytype.csv' NULL 'null' DELIMITER ',' quote '\\\"' csv;"},
{'schools_boundary':"COPY (select id,name,active,boundary_category_id,boundary_type_id,parent_id from schools_boundary) TO '$PWD/load/schools_boundary.csv' NULL 'null' DELIMITER ',' quote '\\\"' csv;"},
{'schools_moitype':"COPY schools_moi_type TO '$PWD/load/schools_moitype.csv' NULL 'null' DELIMITER ',' quote '\\\"' csv;"}, 
{'schools_institutionmanagement':"COPY schools_institution_management TO '$PWD/load/schools_institutionmanagement.csv' NULL 'null' DELIMITER ',' quote '\\\"' csv;"},
{'schools_institutioncategory':"COPY schools_institution_category TO '$PWD/load/schools_institutioncategory.csv' NULL 'null' DELIMITER ',' quote '\\\"' csv;"}, 
{'schools_institution':"COPY (SELECT a.id, a.dise_code, a.name, a.institution_gender, a.active, a.boundary_id, a.cat_id, a.mgmt_id, b.address, b.area, b.instidentification, b.instidentification2, b.landmark, b.pincode, b.route_information FROM schools_institution a LEFT OUTER JOIN schools_institution_address b ON a.inst_address_id = b.id) TO '$PWD/load/schools_institution.csv' NULL 'null' DELIMITER ',' quote '\\\"' csv;"},
{'schools_institution_languages':"COPY schools_institution_languages TO '$PWD/load/schools_institution_languages.csv' NULL 'null' DELIMITER ',' quote '\\\"' csv;"},
{'schools_studentgroup':"COPY (select id,name,section,active,group_type,institution_id from schools_studentgroup) TO '$PWD/load/schools_studentgroup.csv' NULL 'null' DELIMITER ',' quote '\\\"' csv;"},
{'schools_stafftype':"COPY schools_staff_type TO '$PWD/load/schools_stafftype.csv' NULL 'null' DELIMITER ',' quote '\\\"' csv;"},
{'schools_staff':"COPY (SELECT id, first_name, middle_name, last_name, doj, gender, active, institution_id, mt_id, staff_type_id FROM schools_staff) TO '$PWD/load/schools_staff.csv' NULL 'null' DELIMITER ',' quote '\\\"' csv;"},
{'schools_qualificationlist':"COPY schools_staff_qualifications TO '$PWD/load/schools_qualificationlist.csv' NULL 'null' DELIMITER ',' quote '\\\"' csv;"},
{'schools_staff_qualification':"COPY schools_staff_qualification TO '$PWD/load/schools_staff_qualification.csv' NULL 'null' DELIMITER ',' quote '\\\"' csv;"},
{'schools_staffstudentgrouprelation':"COPY (select ssg.id,ssg.active,ssg.academic_id,ssg.staff_id,ssg.student_group_id from schools_staff_studentgrouprelation ssg inner join schools_studentgroup sg on ssg.student_group_id=sg.id ) TO '$PWD/load/schools_staffstudentgrouprelation.csv' NULL 'null' DELIMITER ',' quote '\\\"' csv;"},
{'schools_student':"COPY (SELECT a.id, a.active, b.dob, b.first_name, b.gender, b.last_name, b.middle_name, b.mt_id, b.uid FROM schools_student a INNER JOIN schools_child b on a.child_id = b.id) TO '$PWD/load/schools_student.csv' NULL 'null' DELIMITER ',' quote '\\\"' csv;"},
{'schools_relations':"COPY (select a.id, a.relation_type, a.first_name, a.middle_name, a.last_name, b.id FROM schools_relations a INNER JOIN schools_student b ON a.child_id = b.child_id where a.first_name is not null) TO '$PWD/load/schools_relations.csv' NULL 'null' DELIMITER ',' quote '\\\"' csv;"},
{'schools_studentstudentgrouprelation':"COPY (select ssg.id,ssg.active,ssg.academic_id,ssg.student_id,ssg.student_group_id from schools_student_studentgrouprelation ssg inner join schools_studentgroup sg on ssg.student_group_id=sg.id) TO '$PWD/load/schools_studentstudentgrouprelation.csv' NULL 'null' DELIMITER ',' quote '\\\"' csv;"},
{'schools_programmeinstitution':"COPY (SELECT a.id, a.name, a.description, a.start_date, a.end_date, a.active, a.programme_institution_category_id FROM schools_programme a INNER JOIN schools_assessment b ON a.id = b.programme_id WHERE b.typ = 1 GROUP BY a.id, a.name, a.description, a.start_date, a.end_date, a.active, a.programme_institution_category_id) TO '$PWD/load/schools_programmeinstitution.csv' NULL 'null' DELIMITER ',' quote '\\\"' csv;"},
{'schools_programmestudent':"COPY (SELECT a.id, a.name, a.description, a.start_date, a.end_date, a.active, a.programme_institution_category_id FROM schools_programme a INNER JOIN schools_assessment b ON a.id = b.programme_id WHERE b.typ = 3 GROUP BY a.id, a.name, a.description, a.start_date, a.end_date, a.active, a.programme_institution_category_id) TO '$PWD/load/schools_programmestudent.csv' NULL 'null' DELIMITER ',' quote '\\\"' csv;"},
{'schools_assessmentinstitution':"COPY (SELECT id, name, start_date, end_date, query, active, double_entry, flexi_assessment, primary_field_name,  primary_field_type,  programme_id FROM schools_assessment WHERE typ = 1) TO '$PWD/load/schools_assessmentinstitution.csv' NULL 'null' DELIMITER ',' quote '\\\"' csv;"},
{'schools_assessmentstudent':"COPY (SELECT id, name, start_date, end_date, query, active, double_entry, flexi_assessment, primary_field_name,  primary_field_type,  programme_id FROM schools_assessment WHERE typ = 3) TO '$PWD/load/schools_assessmentstudent.csv' NULL 'null' DELIMITER ',' quote '\\\"' csv;"},
{'schools_questioninstitution':"COPY (SELECT a.id, a.name, a.question_type, a.score_min, a.score_max, a.grade, a.order, a.double_entry, a.active, a.assessment_id FROM schools_question a INNER JOIN schools_assessment b ON a.assessment_id = b.id WHERE b.typ = 1) TO '$PWD/load/schools_questioninstitution.csv' NULL 'null' DELIMITER ',' quote '\\\"' csv;"},
{'schools_questionstudent':"COPY (SELECT a.id, a.name, a.question_type, a.score_min,a.score_max, a.grade, a.order, a.double_entry, a.active, a.assessment_id FROM schools_question a INNER JOIN schools_assessment b ON a.assessment_id = b.id WHERE b.typ = 3) TO '$PWD/load/schools_questionstudent.csv' NULL 'null' DELIMITER ',' quote '\\\"' csv;"},
{'schools_answerinstitution':"COPY (select id, answer_score, answer_grade, double_entry, status, creation_date, last_modified_date, flexi_data, last_modified_by_id, question_id, user1_id, user2_id, active, object_id from schools_answer where content_type_id = 18) TO '$PWD/load/schools_answerinstitution.csv' NULL 'null' DELIMITER ',' quote '\\\"' csv;"},
{'schools_answerstudent':"COPY (select id, answer_score, answer_grade, double_entry, status, creation_date, last_modified_date, flexi_data, last_modified_by_id, question_id, user1_id, user2_id, active, object_id from schools_answer where content_type_id = 24) TO '$PWD/load/schools_answerstudent.csv' NULL 'null' DELIMITER ',' quote '\\\"' csv;"},
{'schools_assessmentstudentgroupassociation':"COPY (select id,active,assessment_id,student_group_id from schools_assessment_studentgroup_association) TO '$PWD/load/schools_assessmentstudentgroupassociation.csv' NULL 'null' DELIMITER ',' quote '\\\"' csv;"},
{'schools_assessmentinstitutionassociation':"COPY (select id,active,assessment_id,institution_id  from schools_assessment_institution_association) TO '$PWD/load/schools_assessmentinstitutionassociation.csv' NULL 'null' DELIMITER ',' quote '\\\"' csv;"}
]


def create_sqlfiles():
  for table in tables:
    for name in table:
      #create the copy to file to get data from ems
      command='echo "'+table[name]+'\">>'+inputdatafile
      system(command)
      #create the copy from file to load data into tada
      filename=os.getcwd()+'/load/'+name+'.csv'
      open(filename,'w',0)
      os.chmod(filename,0666)
      system('echo "COPY '+name+" from '"+filename+"' with csv NULL 'null';"+'\">>'+loaddatafile)

def getdata():
  command="psql -U klp -d "+database+" -f "+inputdatafile
  system(command)



create_sqlfiles()
getdata()

