from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Drive, Student, Instructor, Course, Objective, Member


class DriveForm(forms.ModelForm):

    class Meta:
        model = Drive
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select Student', 'id': 'student'}),
            'instructor': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select Instructor'}),
            'score': forms.TextInput(attrs={'class': '', 'placeholder': ''}),
            'deductions': forms.TextInput(attrs={'class': '', 'placeholder': ''}),
            'hours_driven': forms.TextInput(attrs={'class': '', 'placeholder': ''}),
            'hours_observed': forms.TextInput(attrs={'class': '', 'placeholder': ''}),
            'date': forms.DateInput(attrs={'class': '', 'placeholder': ''}),
            'signature': forms.TextInput(attrs={'class': '', 'placeholder': ''}),
            'comments': forms.TextInput(attrs={'class': '', 'placeholder': ''}),
        }

        exclude = ['hours_driven', 'hours_observed', 'updated', 'student', 'instructor']


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'


class InstructorForm(forms.ModelForm):

    class Meta:
        model = Instructor
        fields = '__all__'


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = '__all__'


class ObjectiveForm(forms.ModelForm):

    class Meta:
        model = Objective
        fields = '__all__'


class MemberForm(forms.ModelForm):

    class Meta:
        model = Member
        fields = '__all__'


class LoginForm():
    pass