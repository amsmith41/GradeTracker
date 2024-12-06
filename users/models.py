from django.db import models
from django.contrib.auth.models import User
'''
from django.db import models
from django.utils import timezone
#from django.contrib.auth.models import User #user model
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=200, null=True) #Indicates that this field can store NULL values in the database. This means the field is optional, and a user can be created without providing a name.
    last_name = models.CharField(max_length=200, null=True)
    is_instructor = models.BooleanField(default=False)
    id_number = models.CharField(unique=True, max_length=20)
    email = models.EmailField(unique=True, null=True) #must be unique, nullable
    bio = models.TextField(null=True) #nullable, proivdes an user where users can write about their bio
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.id_number}" 
'''