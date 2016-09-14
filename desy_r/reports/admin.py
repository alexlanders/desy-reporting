from django.contrib import admin
from .models import Drive, Student, Instructor

# Register your models here.

admin.site.register(Drive)
admin.site.register(Student)
admin.site.register(Instructor)