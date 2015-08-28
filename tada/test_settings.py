from settings import *

DBNAME = DATABASES['default']['NAME']
USER = DATABASES['default']['USER']
PASSWORD = DATABASES['default']['PASSWORD']
print "Inside test_settings.."
print "Test Database name: test_" + DBNAME
print "User name:" + USER
print "Using password from the settings file..."


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'test_' + DBNAME,
        'USER': USER,
        'PASSWORD': PASSWORD,
        'HOST': '',
        'PORT': '',
    }
}

TESTS_STUDENTS_INPUT = {
    'STUDENT_ID1': '429883'

}


try:
    from local_test_settings import *
except:
    pass