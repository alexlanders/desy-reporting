from django.test import TestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from .models import Drive, Student, Instructor, Member


# Create your tests here.

class DriveMethod(TestCase):

    def setUp(self):
        drive_data = {
            "date": "2016-09-24",
            "updated": "2016-09-24",
            "score": 94,
            "deductions": 6,
            "comments": "Not so great.",
            "hours_driven": 1.0,
            "hours_observed": 1.0,
            "signature": True
        }

        new_student = mixer.blend('reports.Student', total_hours_driven=0, total_hours_observed=0)

        for i in range(7):
            new_drive = mixer.blend('reports.Drive', instructor=Instructor.objects.get(id=1), student=new_student,
                                    score=99, deductions=0)
            new_drive.save()

        new_student.save()

        self.student_create = Student.objects.create()
        self.instructor_create = Instructor.objects.create()
        self.drive_create = Drive.objects.create(instructor=self.instructor_create)


        perfect_student_data = {
            "lenses": False,
            "permit": True
        }

        self.perfect_drive = Drive.objects.create(student=self.perfect_student, **drive_data)

    def tearDown(self):
        pass


    def create_test_drive_data(self):
        pass



'''
user = mixer.blend(User, name=mixer.RANDOM('john', 'mike'))
print
user.name
'''
