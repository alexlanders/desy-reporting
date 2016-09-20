from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Student(models.Model):
    #
    user = models.OneToOneField(User)
    lenses = models.NullBooleanField(default=False)
    permit = models.NullBooleanField(default=False)

    def __str__(self):
        return "{0.first_name} {0.last_name}".format(self.user)


class Instructor(models.Model):
    #
    user = models.OneToOneField(User)
    instructor_id = models.PositiveSmallIntegerField(max_length=3)
    school = models.ForeignKey(School, related_name='instructors')

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


class Course(models.Model):
    title = models.CharField(max_length=96)
    course_id = models.PositiveSmallIntegerField(max_length=3)
    start_date = models.DateField(auto_now=False)
    end_date = models.DateField(auto_now=False)
    duration = models.DurationField()
    is_complete = models.BooleanField(default=False)
    school = models.ForeignKey(related_name='courses', null=True)

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


