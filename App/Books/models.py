from django.db import models
import uuid
from uuid import uuid4


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.first_name + " " + self.last_name + ".." + self.email


class Book(models.Model):
    id = models.UUIDField(default=uuid4(), primary_key=True)
    title = models.CharField(max_length=100)
    locccn = models.IntegerField(max_length=30)

    # author  = models.ForeignKey(on_delete=models.CASCADE)
    def __str__(self):
        return self.title
