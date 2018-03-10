
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "foodtasker.settings")

application = get_wsgi_application()

#Use this to serve static file on heroku
from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)
