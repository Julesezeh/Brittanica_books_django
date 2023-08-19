from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    user_name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    email = models.CharField(max_length=100, blank=False, null=False)


class Book(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False,unique=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    locccn = models.IntegerField(blank=False,null=False)