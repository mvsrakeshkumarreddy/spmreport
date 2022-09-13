# admin.py
from django.contrib import admin

from .models import *


#from django.contrib.auth.models import User
#from django.contrib.auth.admin import UserAdmin

admin.site.register(User)
#admin.site.register(Spm)