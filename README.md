tada
====

That's All Data. Akshara's data entry/management system.

### Code

    git clone git@github.com:klpdotorg/tada.git

### Setup virualenv using virtualenvwrapper.

    pip install virtualenvwrapper
    
Add these lines to your .bashrc and source it

    # add virtualenv wrappers
    export WORKON_HOME=$HOME/.virtualenvs
    export PROJECT_HOME=$HOME/Devel
    source /usr/local/bin/virtualenvwrapper.sh

Finally source .bashrc using the following command
    
    source ~/.bashrc

Create and activate the virtualenv

    mkvirtualenv tada
    workon tada
   
### Install requirements

    pip install -r requirements/base.txt

### Create user klp in postgres

    createuser klp --superuser

User klp is needed to make the migrations work. Otherwise, there will be a FATAL error referencing the klp role. It needs to be superuser so that the copy command works.

The default peer authentication might not work if you're accessing the db as another user. So either set an `md5` password authentication system or `trust` all local connections.

    emacs -nw /etc/postgresql/9.3/main/pg_hba.conf

Edit:

    local   all   all   peer

To:

    local   all   all   trust

### Install and create a local database

    sudo apt-get install postgresql-9.3
    sudo apt-get install postgresql-9.3-postgis-2.1
    sudo -u postgres createdb -E UTF8 -O klp -T template0 klpproduction

### Create a Local settings file

    touch tada/local_settings.py

### Setup your database

Install Postgres 9.3 or above. Have the following configuration in your local_settings.py file.

    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'your_db_name',
        'USER': 'your_db_username',
        'PASSWORD': 'your_db_password',
        'HOST': '',
        'PORT': '',
        }
    }

Run:

    python manage.py migrate

### To import old data refer to README.md in imports directory


### Run the application

    python manage.py runserver

Visit `http://127.0.0.1:8000/`

### Code Formattng guidelines
See PEP8 @ https://www.python.org/dev/peps/pep-0008/
