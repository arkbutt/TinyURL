from django.db import models

from mongoengine import *


class URL(Document):
    hash = StringField(max_length=200)
    original_url = StringField(max_length=400)
