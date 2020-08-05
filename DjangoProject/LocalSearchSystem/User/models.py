from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.

class WikiNewsUser(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200, null=True, unique=True)
    password = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=True, blank=True)

    class Meta:
        db_table = 'WikiNewsUser'
