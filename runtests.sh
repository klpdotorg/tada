#!/bin/bash
# Script usage: runtests.sh <Optional createDB: false>
# Example: To use existing test DB and not create a new one, use ./runtests.sh skipdbcreate
#This script runs all the existing unit tests for the users, schools and stories apps.
# You will need to create a "test" db by cloning the main databasee (eg. createdb -T klpwww_ver4 test_klpwww_ver4 )
#The name of the "test" DB should be entered in the dubdubdub/local_test_settings.py file. Please see those files for further instructions. 


# Create the test database from the dev DB

#Read the local settings file and get the name of the DB. Used a python script to read the DB name from DJango settings.
# Maybe a better way of doing this?
CREATE_DB=true

if [ $# -eq 0 ]; then
    echo Usage: `basename $0` dbuser createtestdbboolean
    exit
fi 

if [ $# -ge 1 ]; then
    DB_USER=$1
    if [ -z $2 ]; then 
      $CREATE_DB = $2
    fi
fi



# Call script to create test database if CREATE_DB is true

if [ "$CREATE_DB" == "true" ]; then
    testDB=''
    source createTestDb.sh $DB_USER
    exit_status=$?
    if [ $exit_status -ne 0 ]; then
        exit $exit_status
    fi
fi

# Start running the unit tests...

python manage.py test tests --settings tests.test_settings

# Now, clean up the test database (if it was created at all in the first place)
if [ "$CREATE_DB" == "true" ]; then
    source deleteTestDb.sh $testDB $DB_USER
fi


