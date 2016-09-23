from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    user = models.OneToOneField(User)
    total_hours_driven = models.PositiveSmallIntegerField(default=False, null=True)
    total_hours_observed = models.PositiveSmallIntegerField(default=False, null=True)

# Create your models here.
class Student(Member):
    #
    lenses = models.NullBooleanField(default=False)
    permit = models.NullBooleanField(default=False)

    def __str__(self):
        return "{0.first_name} {0.last_name}".format(self.user)


class School(models.Model):
    name = models.CharField(max_length=120, null=True)

    def __str__(self):
        return "{}".format(self.name)


class Instructor(Member):
    #
    instructor_id = models.PositiveSmallIntegerField()
    school = models.ForeignKey(School, related_name='instructors', null=True, blank=True)

    def __str__(self):
        return "{0.first_name} {0.last_name}".format(self.user)


class Drive(models.Model):
    # Attributes for drives in db
    student = models.ForeignKey(Student, related_name='drives', null=True)
    instructor = models.ForeignKey(Instructor, related_name='drives', null=True)
    date = models.DateField(auto_now=False)
    updated = models.DateField(auto_now=False, null=True)
    score = models.PositiveSmallIntegerField()
    deductions = models.IntegerField()
    comments = models.TextField(max_length=256)
    hours_driven = models.FloatField(default=1)
    hours_observed = models.FloatField(default=1)
    signature = models.NullBooleanField(default=False)

    def absolute_url(self):
        return '/drive/detail/{}'.format(self.id)

    def __str__(self):
        return "Instructor: {} - Student: {}, Score: {}".format(self.instructor, self.student, self.score)

    def save(self, *args, **kwargs): #TODO double-check update functionality
        self.student.total_hours_driven += self.hours_driven
        self.student.total_hours_observed += self.hours_observed
        super(Drive, self).save(*args, **kwargs)


class Course(models.Model):
    title = models.CharField(max_length=96)
    course_id = models.PositiveSmallIntegerField()
    start_date = models.DateField(auto_now=False)
    end_date = models.DateField(auto_now=False)
    duration = models.DurationField()
    is_complete = models.BooleanField(default=False)
    school = models.ForeignKey(School, related_name='courses', null=True)

    def __str__(self):
        return "{}".format(self.title)

    def save(self, *args, **kwargs):
        self.duration = self.end_date - self.start_date
        return super(Course, *args, **kwargs)


class Objective(models.Model):
    # Objectives for course
    target = models.IntegerField(choices=())
    description = models.CharField(max_length=128)
    course = models.ForeignKey(Course, related_name='objectives')

    def __str__(self):
        return "{} {}".format(self.man_id, self.desc)


