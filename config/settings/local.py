from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='#@liw0e3p+s3)^l0k!_fm6jv^^hf$z2b4g4cos5yx-fbo0(&(b')

DEBUG = env.bool('DJANGO_DEBUG', default=True)
