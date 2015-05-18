tada
====

That's All Data. Akshara's data entry/management system.

### Code

    git clone git@github.com:klpdotorg/tada.git

### Setup virualenv using virtualenvwrapper

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

### Run the application

    python manage.py runserver

Visit `http://127.0.0.1:8000/`
