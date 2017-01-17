SELECT SETVAL('public.auth_group_id_seq', COALESCE(MAX(id), 1) ) FROM public.auth_group;
SELECT SETVAL('public.auth_group_permissions_id_seq', COALESCE(MAX(id), 1) ) FROM public.auth_group_permissions;
SELECT SETVAL('public.auth_permission_id_seq', COALESCE(MAX(id), 1) ) FROM public.auth_permission;
SELECT SETVAL('public.auth_user_groups_id_seq', COALESCE(MAX(id), 1) ) FROM public.auth_user_groups;
SELECT SETVAL('public.auth_user_id_seq', COALESCE(MAX(id), 1) ) FROM public.auth_user;
SELECT SETVAL('public.auth_user_user_permissions_id_seq', COALESCE(MAX(id), 1) ) FROM public.auth_user_user_permissions;
SELECT SETVAL('public.django_admin_log_id_seq', COALESCE(MAX(id), 1) ) FROM public.django_admin_log;
SELECT SETVAL('public.django_content_type_id_seq', COALESCE(MAX(id), 1) ) FROM public.django_content_type;
SELECT SETVAL('public.django_migrations_id_seq', COALESCE(MAX(id), 1) ) FROM public.django_migrations;
SELECT SETVAL('public.schools_academicyear_id_seq', COALESCE(MAX(id), 1) ) FROM public.schools_academicyear;
SELECT SETVAL('public.schools_answerinstitution_id_seq', COALESCE(MAX(id), 1) ) FROM public.schools_answerinstitution;
SELECT SETVAL('public.schools_answerstudent_id_seq', COALESCE(MAX(id), 1) ) FROM public.schools_answerstudent;
SELECT SETVAL('public.schools_assessment_id_seq', COALESCE(MAX(id), 1) ) FROM public.schools_assessment;
SELECT SETVAL('public.schools_assessmentinstitutionassociation_id_seq', COALESCE(MAX(id), 1) ) FROM public.schools_assessmentinstitutionassociation;
SELECT SETVAL('public.schools_assessmentstudentgroupassociation_id_seq', COALESCE(MAX(id), 1) ) FROM public.schools_assessmentstudentgroupassociation;
SELECT SETVAL('public.schools_boundary_id_seq', COALESCE(MAX(id), 1) ) FROM public.schools_boundary;
SELECT SETVAL('public.schools_boundarycategory_id_seq', COALESCE(MAX(id), 1) ) FROM public.schools_boundarycategory;
SELECT SETVAL('public.schools_boundarytype_id_seq', COALESCE(MAX(id), 1) ) FROM public.schools_boundarytype;
SELECT SETVAL('public.schools_compensationauditlog_id_seq', COALESCE(MAX(id), 1) ) FROM public.schools_compensationauditlog;
SELECT SETVAL('public.schools_institution_id_seq', COALESCE(MAX(id), 1) ) FROM public.schools_institution;
SELECT SETVAL('public.schools_institution_languages_id_seq', COALESCE(MAX(id), 1) ) FROM public.schools_institution_languages;
SELECT SETVAL('public.schools_institutioncategory_id_seq', COALESCE(MAX(id), 1) ) FROM public.schools_institutioncategory;
SELECT SETVAL('public.schools_institutionmanagement_id_seq', COALESCE(MAX(id), 1) ) FROM public.schools_institutionmanagement;
SELECT SETVAL('public.schools_moitype_id_seq', COALESCE(MAX(id), 1) ) FROM public.schools_moitype;
SELECT SETVAL('public.schools_programme_id_seq', COALESCE(MAX(id), 1) ) FROM public.schools_programme;
SELECT SETVAL('public.schools_qualificationlist_id_seq', COALESCE(MAX(id), 1) ) FROM public.schools_qualificationlist;
SELECT SETVAL('public.schools_question_id_seq', COALESCE(MAX(id), 1) ) FROM public.schools_question;
SELECT SETVAL('public.schools_relations_id_seq', COALESCE(MAX(id), 1) ) FROM public.schools_relations;
SELECT SETVAL('public.schools_staff_id_seq', COALESCE(MAX(id), 1) ) FROM public.schools_staff;
SELECT SETVAL('public.schools_staff_qualification_id_seq', COALESCE(MAX(id), 1) ) FROM public.schools_staff_qualification;
SELECT SETVAL('public.schools_staffstudentgrouprelation_id_seq', COALESCE(MAX(id), 1) ) FROM public.schools_staffstudentgrouprelation;
SELECT SETVAL('public.schools_stafftype_id_seq', COALESCE(MAX(id), 1) ) FROM public.schools_stafftype;
SELECT SETVAL('public.schools_student_id_seq', COALESCE(MAX(id), 1) ) FROM public.schools_student;
SELECT SETVAL('public.schools_studentgroup_id_seq', COALESCE(MAX(id), 1) ) FROM public.schools_studentgroup;
SELECT SETVAL('public.schools_studentstudentgrouprelation_id_seq', COALESCE(MAX(id), 1) ) FROM public.schools_studentstudentgrouprelation;