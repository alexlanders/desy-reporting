from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Drive, Student, Instructor


class DriveForm(forms.ModelForm):

    class Meta:
        model = Drive
        exclude = ['hours_driven', 'hours_observed', 'updated', 'student', 'instructor']


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'


class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = '__all__'


class LoginForm():
    pass