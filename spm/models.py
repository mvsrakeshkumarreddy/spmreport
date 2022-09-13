# models.py

from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager




class User(AbstractUser):
    username = None
    full_name = models.CharField(max_length = 150)
    crew_ID = models.CharField(max_length = 7, unique = True)
    station = models.CharField(max_length = 3)
    employee_ID = models.CharField(max_length = 11)
    appointment_date = models.DateField()
    #some    = models.CharField(max_length = 100)
    
   

    objects = UserManager()

    USERNAME_FIELD = 'crew_ID'

    REQUIRED_FIELDS = []


