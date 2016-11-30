# Procedure for importing legacy data from EMS to new structure

1. Get dump of ems data and copy it to imports directory (To avoid role errors you can try getting it with --no-owner flag while doing pg_dump)
2. Modify createemsfromdump.sh script to point it to correct dump
3. Run createemsfromdump.sh script (This will create an ems database with the data from the dump)
   (You might get Role errors depending on how the dump was created. These can be ignored.)
4. Modify importdata.py script to point to correct tada database and correct ems database.
5. Run importdata.py script
Check errors to make sure that the scripts have run properly.
