"""
from django.db import models
from django.contrib.auth.models import User
from django.core.cache import cache 
from django import forms
import datetime
from mysite import settings

# Create your models here.
class ProfilePicture(models.Model):
    user = models.ForeignKey(User, related_name='profile_picture', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=f'users/{user}', default='default_profile.png')

    def __str__(self):
        return self.image.url

class Data(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.first_name
"""

from django.db import models
from django.contrib.auth.models import User
from django.core.cache import cache 
from django import forms
import datetime
from mysite import settings

class Info(models.Model):
	OCCUPATION_CHOICES = [
    ("1", "Criminal lawyer"),
    ("2", "Environmental lawyer"),
    ("3", "Family lawyer"),
    ("4", "Corporate lawyer"),
    ("5", "Civil lawyer"),
	("6", "Tax lawyer"),
	("7", "Cyber lawyer"),
	("8", "Government lawyer"),
	("9", "Military lawyer"),
	("10", "Others")
    ]
	user = models.ForeignKey(User, related_name='info', on_delete=models.CASCADE)
	occupation = models.CharField(
        max_length=4,
        choices=OCCUPATION_CHOICES,
    )
	bio = models.CharField(max_length=1000)
	phone = models.IntegerField()
    