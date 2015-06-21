--USE this table queries if you are creating the new table structures from scratch

CREATE TABLE schools_assessmentinstitution (
 id integer, 
 programme_id integer,
 name varchar(100),
 start_date date,
 end_date date,
 query varchar(500),
 active integer,
 typ integer,
 double_entry boolean,
 flexi_assessment  boolean, 
 primary_field_name varchar(500),
 primary_field_type integer
);

CREATE TABLE schools_answerinstitution ( 
 id                  integer, 
 question_id         integer, 
 answer_score        numeric(10,2),
 answer_grade        varchar(30),
 double_entry        integer, 
 status              integer,
 creation_date       date,   
 last_modified_date  date,    
 flexi_data          varchar(30), 
 last_modified_by_id integer,
 user1_id            integer, 
 user2_id            integer
);

CREATE TABLE schools_questioninstitution (
 id              integer,     
 name            varchar(200),
 question_type   integer, 
 score_min       numeric(10,2), 
 score_max       numeric(10,2),
 grade           varchar(100), 
 "order"         integer, 
 double_entry    boolean, 
 active          integer,
 assessment_id   integer
);

CREATE TABLE schools_institutionnew (
 id                  integer,
 dise_code           varchar(14),
 name                varchar(300), 
 institution_gender  varchar(10),
 active              integer,
 boundary_id         integer,
 cat_id              integer,
 mgmt_id             integer,
 address             varchar(1000),
 area                varchar(200), 
 instidentification  varchar(1000),
 instidentification2 varchar(1000), 
 landmark            varchar(1000),
 pincode             varchar(100),
 route_information   varchar(500)
);

CREATE TABLE schools_studentnew (
 id          integer,
 active      integer,
 dob         date,
 first_name  varchar(50),
 gender      varchar(10),
 last_name   varchar(50),
 middle_name varchar(50),
 mt_id       integer,
 uid         varchar(100)
);


CREATE TABLE schools_relationsnew (
 id            integer,
 relation_type varchar(10),
 first_name    varchar(100),
 middle_name   varchar(50),
 last_name     varchar(50),
 student_id    integer 
);

