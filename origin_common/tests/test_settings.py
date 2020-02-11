SECRET_KEY = 'fake-key'
INSTALLED_APPS = [
    "tests",
]
DATABASES={
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "testdb",
        # "USER": "gitlab",
        # "PASSWORD": "gitlabpwd",
        # "HOST": "postgres",
    },
}
