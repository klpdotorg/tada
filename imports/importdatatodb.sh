echo "##################################"
echo "START_LOG"
date
echo "##################################"

recreate_tables=off
dbname="klpproduction_new"

while getopts d:t opt
do
    case "$opt" in
        t)  recreate_tables=on;;
        d)  dbname="$OPTARG";;
        \?)       # unknown flag
            echo >&2
            echo "usage: $0 [-t]"
            echo
            echo "-t   Regenerates the new EMS table structure from CSV dumps"
      exit 1;;
    esac
done
shift `expr $OPTIND - 1`

if [ $recreate_tables = on ]; then
    echo "Dropping temporary tables"
    psql -U klp $dbname < imports/sql/droptables.sql
    echo "Creating tables"
    workon tada
    python manage.py migrate
    for f in `pwd`/data/ems/*.csv;
    do
        filename=$(basename $f .csv)
        echo "Inserting data to temp table: $filename"
        psql -U klp -d $dbname -c "copy ems_$filename from '$f' CSV HEADER"
        # FIXME : Insert statement to create indices
	psql -U klp -d $dbname -c "analyze ems_$filename"
	
    done
fi
