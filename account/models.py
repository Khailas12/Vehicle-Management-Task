from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    is_super_admin = models.BooleanField('Super Admin', default=False)
    is_admin = models.BooleanField('Admin', default=False)
    is_user = models.BooleanField('User', default=False)

    
