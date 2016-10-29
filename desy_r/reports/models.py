from django.db import models
from django.contrib.auth.models import User
from .choices import COUNTRIES, STATES, PROVINCES


class Member(models.Model):
    user = models.OneToOneField(User)


class School(models.Model):
    name = models.CharField(max_length=120, null=True)

    def __str__(self):
        return "{}".format(self.name)


class Instructor(Member):
    #
    instructor_id = models.PositiveSmallIntegerField(null=True)
    school = models.ForeignKey(School, related_name='instructors', null=True, blank=True)

    def __str__(self):
        return "{0.first_name} {0.last_name}".format(self.user)


class Course(models.Model):
    title = models.CharField(max_length=96)
    course_id = models.PositiveSmallIntegerField()
    start_date = models.DateField(auto_now=False)
    end_date = models.DateField(auto_now=False)
    duration = models.DurationField(null=True)
    is_complete = models.BooleanField(default=False)
    instructor = models.ForeignKey(Instructor, related_name='instructor')
    school = models.ForeignKey(School, related_name='courses', null=True)

    def __str__(self):
        return "{}".format(self.title)

    def save(self, *args, **kwargs):
        self.duration = self.end_date - self.start_date
        return super(Course, self).save(*args, **kwargs)


class Student(Member):
    #
    lenses = models.NullBooleanField(default=False)
    permit = models.NullBooleanField(default=False)
    courses = models.ForeignKey(Course, related_name='students', null=True)
    total_hours_driven = models.PositiveSmallIntegerField(default=0, null=True)
    total_hours_observed = models.PositiveSmallIntegerField(default=0, null=True)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return '{0.first_name} {0.last_name}'.format(self.user)


class Drive(models.Model):
    # Attributes for drives in db
    student = models.ForeignKey(Student, related_name='drives', null=True)
    instructor = models.ForeignKey(Instructor, related_name='instructors', null=True)
    course = models.ForeignKey(Course, related_name='course', null=True)
    date = models.DateField(auto_now=False)
    updated = models.DateField(auto_now=False, null=True)
    score = models.PositiveSmallIntegerField()
    deductions = models.IntegerField()
    comments = models.TextField(max_length=256)
    hours_driven = models.FloatField(default=1)
    hours_observed = models.FloatField(default=1)
    signature = models.NullBooleanField(default=False)

    def update_hours_driven(self):
        if self.id is None:
            self.student.total_hours_driven += self.hours_driven
            self.student.total_hours_observed += self.hours_observed
            self.student.save()
        return self

    def absolute_url(self):
        return '/drive/detail/{}'.format(self.id)

    def __str__(self):
        return "Instructor: {} - Student: {}, Score: {}".format(self.instructor, self.student, self.score)

    def save(self, *args, **kwargs):
        self.update_hours_driven()

        super(Drive, self).save(*args, **kwargs)


class Objective(models.Model):
    # Objectives for course
    course = models.ManyToManyField(Course)
    objective_code = models.CharField(max_length=24, null=True)
    target = models.IntegerField(choices=())
    behavior_name = models.CharField(max_length=250, null=True)
    chapter = models.PositiveSmallIntegerField(null=True)
    notes = models.CharField(max_length=250, null=True)
    state = models.CharField(max_length=2, choices=STATES, null=True)

    def __str__(self):
        return "{} {}".format(self.course, self.description)

'''
Future features:

- Allowing objective additions to directly affect tablet app for drive to update automatically
- Live adding of all available objectives for drive. "I want these 30 objectives to be covered in this drive"
- Show all progress in student details page.
'''