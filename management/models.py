from django.db import models
from uuid import uuid4


# Create your models here.
class Trainer(models.Model):
    name = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    role = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Details(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    trainer_name = models.CharField(max_length=30)
    student_name = models.CharField(max_length=30)
    mob_no = models.CharField(max_length=10)
    course = models.CharField(max_length=30)
    duration = models.CharField(max_length=10)
    time_slot = models.CharField(max_length=10)

    def __str__(self):
        return self.trainer_name
