from django.contrib import admin
from .models import Drive, Student, Instructor, School, Course

# Register your models here.

admin.site.register(Drive)
admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(School)
admin.site.register(Course)