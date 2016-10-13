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

        fields = ['student', 'instructor', 'date', 'score', 'deductions', 'comments']


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['lenses', 'permit']


class InstructorForm(forms.ModelForm):

    class Meta:
        model = Instructor
        fields = ['instructor_id', 'school']


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['title', 'course_id', 'start_date', 'end_date', 'is_complete', 'school']


class ObjectiveForm(forms.ModelForm):

    class Meta:
        model = Objective
        fields = ['course', 'objective_code', 'target', 'behavior_name', 'chapter', 'notes', 'state']


class MemberForm(forms.ModelForm):

    class Meta:
        model = Member
        fields = ['user']


class LoginForm():
    pass