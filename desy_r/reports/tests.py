from django.test import TestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from .models import Drive, Student, Instructor, Member


# Create your tests here.

class TestDriveMethod(TestCase):

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

        perfect_student_data = {
            "lenses": False,
            "permit": True
        }

        self.perfect_user1 = User.objects.create(username='test_user1', password='1234abcd')
        self.perfect_user2 = User.objects.create(username='test_user2', password='1234abcd')
        # self.perfect_member1 = Member.objects.create(user=self.perfect_user1)
        # self.perfect_member2 = Member.objects.create(user=self.perfect_user2)
        self.perfect_student = Student.objects.create(user=self.perfect_user2, **perfect_student_data)
        self.perfect_instructor = Instructor.objects.create(user=self.perfect_user1, instructor_id=1)
        self.perfect_drive = Drive.objects.create(instructor=self.perfect_instructor,
                                                  student=self.perfect_student, **drive_data)

        self.random_drive = mixer.blend('reports.Drive', score=90, deductions=1)

    def tearDown(self):
        self.perfect_student.delete()
        self.perfect_instructor.delete()
        self.perfect_drive.delete()
        self.perfect_user1.delete()
        self.perfect_user2.delete()
        # self.perfect_member1.delete()
        # self.perfect_member2.delete()

    def test_perfect_student_total_hours_driven_updates_on_Drive_save(self):
        self.perfect_drive.save()
        self.assertEqual(self.perfect_student.total_hours_driven, 1.0)
        next_drive = {
            "date": "2016-09-26",
            "updated": "2016-09-26",
            "score": 98,
            "deductions": 2,
            "comments": "Much improvement.",
            "hours_driven": 2.0,
            "hours_observed": 2.0,
            "signature": True
        }
        drive = Drive.objects.create(instructor=self.perfect_instructor,
                                     student=self.perfect_student, **next_drive)
        drive.save()
        self.assertEqual(self.perfect_student.total_hours_driven, 3.0)

    def test_random_student_total_hours_driven_updates_on_Drive_save(self):

        random_drive_hours_driven = self.random_drive.hours_driven

        self.assertEqual(self.random_drive.hours_driven, random_drive_hours_driven)

        next_drive = mixer.blend('reports.Drive', student=self.random_drive.student,
                                 instructor=self.random_drive.instructor, deductions=1, score=91)

        total_random_hours = random_drive_hours_driven + next_drive.hours_driven

        self.assertEqual(self.random_drive.hours_driven, total_random_hours)