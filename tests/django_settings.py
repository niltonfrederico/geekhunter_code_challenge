from abundantia_api.settings.development import *  # noqa

CI = env.bool("CI", default=False)

CELERY_ALWAYS_EAGER = True
