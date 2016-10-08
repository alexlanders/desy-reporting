from reports.models import *
import random
from mixer.backend.django import mixer


def populate_random_student_drives(amount):
    for i in range(amount):
        instructor = Instructor.objects.get(instructor_id=1)
        new_student = mixer.blend('reports.Student', total_hours_driven=0, total_hours_observed=0)
        random_number = [1, 2, 3, 4, 5, 6]
        number = random.choice(random_number)
        for x in range(number):
            random_scores = list(range(101))
            random_score = random.choice(random_scores)
            new_drive = mixer.blend('reports.Drive', instructor=instructor, student=new_student,
                                    score=random_score, deductions=0)
            new_drive.save()

        new_student.save()
        print('Saved student successfully.')
    print('All Done.')
    return None