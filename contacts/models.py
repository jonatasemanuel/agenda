from django.db import models
from django.utils import timezone


# Create your models here.
class Status(models.Model):
    # id = models.IntegerField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100, blank=True)
    creation_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
