SECRET_KEY = "fake-key"
INSTALLED_APPS = [
    "origin_common",
    "tests",
]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "testdb",
        "USER": "gitlab",
        "PASSWORD": "gitlabpwd",
        "HOST": "postgres",
    },
}
