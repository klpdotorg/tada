## Semi-automated approach for migrating data 	
You can migrate data to the new format using one of the two following methods

### Common steps
Recreate the schema from django.
*  Create a database using createdb
```
$ sudo -u postgres createdb -E UTF8 -O klp -T template0 klp_transform 
```
*  Change your local settings to point to new DB. See README.md in root 
folder for this.
*  Run migrate to create the empty data tables
```
$ python manage.py migrate
```
* If all has gone well and you have not got any errors (you might get a 
warning or two - ignore for now) then the database has been created with 
the tables.
* You can check using the following command at the postgres prompt
```
$ sudo -u postgres psql klp_transform
psql (9.3.7)
Type "help" for help.

klp_transform=# \d+ <ENTER>
```
*  Now go ahead and try method 1 or 2 to get data into tables.

* Now you can run the commands listed in imports/sql/transform.sql on the
psql commandline to alter/fill the created tables with data.

### Method 1 - Migrating data from old EMS dump
* Login to new EMS machine (as user klp) and download the file
klpproduction_feb18.sql.bz2. This is a large file so it might take a few 
hours.
* Unzip the file using the command
```
$ bunzip klpproduction_feb18.sql.bz2
```
* The above command might take a while as the file will be large about 3.5GB.
Now import the file using the command
```
$ sudo -u postgres psql klp_transform < klpproduction_20-05-2015_02_45
```
* Check the inserted data by using the command below and doing select 
limit/count on some of the tables.
```
$ sudo -u postgres psql klp_transform
psql (9.3.7)
Type "help" for help.

klp_transform=# \d+ <ENTER>
```

### Method 2 - Migrating from individual tables
You can ask @devi or @brijesh to give you a CSV dump of individual tables and 
import the tables from the CSVs. Please see the imports/sql/transform.sql 
file to see the groups of tables you can import tables. Also double check the 
migrated schema above and see if there are any dependencies on other foreign 
tables. Also check imports/importdatatodb.sh script to get an idea how this 
will look when automated completely. You can copy CSVs into the database 
using \COPY command of postgres.
