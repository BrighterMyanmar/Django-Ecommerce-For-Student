from django.db import models
from django.contrib.auth.models import User

User._meta.get_field('email')._unique=True
# User._meta.get_field('phone')._unique=True

