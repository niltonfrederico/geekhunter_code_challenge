from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "c@vc)dkhlqrutz3y$1y!7^1t_()a(y@$n3z-g@kgw_e$%=goq&"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    "default": env.db(default="mysql://root:password@abundantia_mysql:3306/abundantia")
}
