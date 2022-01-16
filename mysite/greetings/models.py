import email
from django.db import models


class Greetings(models.Model):
    email = models.CharField(max_length=40)