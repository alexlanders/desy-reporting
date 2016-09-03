from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Drive(models.Model):
    # Attributes for drives in db
    date = models.DateField(auto_now=False)
    updated = models.DateField(auto_now=False)
    score = models.PositiveSmallIntegerField()
    deductions = models.IntegerField() #TODO: Can deductions be negative?
    comments = models.CharField(max_length=256)
    hrs_driven = models.FloatField()
    hrs_observed = models.FloatField()
    signature = models.NullBooleanField()


class Maneuver(models.Model):
    # Maneuvers inside of Drives
    man_id = models.CharField(max_length=5)
    desc = models.CharField(max_length=128)


class Student(models.Model):
    #
    user = models.OneToOneField(User)
    lenses = models.BooleanField(default=False)
    permit = models.BooleanField(default=False)


class Instructor(models.Model):
    #
    user = models.OneToOneField(User)
