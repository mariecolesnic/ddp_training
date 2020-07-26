from .base import*

DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'PASSWORD': os.environ.get("POSTGRES_PASSWORD", "112233"),
        'USER': 'postgres',
        'HOST': os.environ.get("POSTGRES_HOST", "localhost"),
        'PORT': 5432,
    }
}
