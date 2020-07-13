from django.db import models

# Create your models here.

class User(models.Model):
    userid = models.AutoField(primary_key = True)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    status = models.CharField(max_length=45)
    usertype = models.CharField(max_length=45)

    class Meta:
        db_table = 'User'