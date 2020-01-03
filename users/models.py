from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    
    gender = models.IntegerField(null=True, blank=True, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField(null=True, blank=True)
    # age.help_text = 'something'