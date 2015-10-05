#!/bin/bash
#This script creates a test database from the existing main dev database. Reads the local_settings file to retrieve the DB
#name and then creates the clone.
if [ $# -eq 0 ]; then
    echo "Please pass in the DB username as argument."
    exit 1
fi
if [ -z "$2" ]; then
    echo "Please supply a valid db user name"
    exit 2
fi
dbUserName=$1
mainDBName=$(python -m read_local_settings)
exit_status=$?
if [ $exit_status -ne 0 ]; then
    echo "Failure to read settings file from django. Please check if settings file exists. Aborting unit tests"
    exit $exit_status
else
    echo "Database being used by app is $mainDBName"
fi

#Use the db name to create a clone
testDB="test_$mainDBName"
echo "Creating database $testDB as a clone of $mainDBName...."
sudo -i -u $dbUserName createdb -T $mainDBName $testDB
exit_status=$?
if [ $exit_status -ne 0 ]; then
    echo "Failure creating a test DB. Aborting unit tests"
    exit $exit_status
else
    echo "Created $testDB successfully..."
fi