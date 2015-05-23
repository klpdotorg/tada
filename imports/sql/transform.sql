-- schools_academic_year
ALTER TABLE ems_schools_academic_year TO schools_academic_year;
ALTER TABLE schools_academic_year ADD start_year smallint; 
ALTER TABLE schools_academic_year ADD end_year smallint;
update schools_academic_year set start_year = (LEFT(name,4))::int2
update schools_academic_year set end_year = (RIGHT(name,4))::int2;` 
