"""
Django settings for tada project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+6*p_*^5_p2mna5^+i(em#&1)xk_b0i2n_h!6_rr$s6c@+$21q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'accounts',
    'common',
    'django_extensions',
    'djoser',
    'guardian',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_docs',
    'schools',
    'tests',
    'easyaudit',
)

MIDDLEWARE_CLASSES = (
    'common.middleware.ProcessExceptionMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'easyaudit.middleware.easyaudit.EasyAuditMiddleware',
)

DJANGO_EASY_AUDIT_WATCH_LOGIN_EVENTS = False
DJANGO_EASY_AUDIT_UNREGISTERED_CLASSES_EXTRA = [
    'admin.LogEntry',
    'auth.Permission',
    'auth.Group',
    'auth.User',
    'contenttypes.ContentType',
    'sessions.Session',
    'guardian.UserObjectPermission',
    'guardian.GroupObjectPermission',
    'authtoken.Token',
    'schools.BoundaryCategory',
    'schools.BoundaryType',
    'schools.Boundary',
    'schools.InstitutionCategory',
    'schools.MoiType',
    'schools.InstitutionManagement',
    'schools.StaffType',
    'schools.QualificationList',
    'schools.AcademicYear',
    'schools.Programme',
    'schools.Relations',
    'schools.StudentGroup',
    'schools.StudentStudentGroupRelation',
    'schools.StaffStudentGroupRelation',
    'schools.Assessment',
    'schools.AssessmentStudentGroupAssociation',
    'schools.AssessmentInstitutionAssociation',
    'schools.Question',
    'tests.User',
    'tests.Organisation',
    'tests.Membership',
    'easyaudit.CRUDEvent',
    'easyaudit.LoginEvent'
]

ROOT_URLCONF = 'tada.urls'

WSGI_APPLICATION = 'tada.wsgi.application'

TEST_RUNNER = 'common.nodbtestrunner.NoDbTestRunner'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'klpproduction',
        'USER': 'klp',
        'PASSWORD': 'klp',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "/static")

REST_FRAMEWORK = {
    'PAGE_SIZE': 20,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
        'accounts.permissions.TadaBasePermission',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
}

AUTHENTICATION_BACKENDS = (
    'accounts.backends.EmailOrUsernameModelBackend',
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend',
)

CORS_ORIGIN_ALLOW_ALL = True


try:
    from local_settings import *
except ImportError:
    pass
