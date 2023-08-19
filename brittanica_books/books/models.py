from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100, null=False,blank=True)
    last_name = models.CharField(max_length=100,blank=True)
    user_name = models.CharField(max_length=100, blank=True, unique=True)
    email = models.CharField(max_length=100, null=False, blank=True)


class Book(models.Model):
    title = models.CharField(max_length=100, blank=True, null=False,unique=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=False)
    description = models.TextField(max_length=250)
    locccn = models.IntegerField(blank=True,null=False)