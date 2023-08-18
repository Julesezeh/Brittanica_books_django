from django.db import models
import uuid
from uuid import uuid4


# Create your models here.
class Author(models.Model):
    username = models.CharField(max_length=50, null=False, blank=False)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)

    def __str__(self):
        return self.first_name + " " + self.last_name + ".." + self.email


class Book(models.Model):
    id = models.UUIDField(default=uuid4(), primary_key=True, null=False, blank=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    locccn = models.IntegerField(null=False, blank=False)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=False, blank=False
    )

    def __str__(self):
        return self.title
