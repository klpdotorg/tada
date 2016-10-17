#This script is to be used to create a db from a dump.

database='emstemp'
dump='klp_production_june22_2016_01-08-2016_19_05'

#drop the db if it already exists
dropdb -U klp $database
createdb -U klp -E UTF8 -O klp -T template0 $database

#put the  data from dump into the new database
pg_restore $dump -U klp -d $database 1>output 2>error &

#remove inccorect data from new db.
psql -U klp -d $database -f cleanems.sql
