from django.shortcuts import render
from django.http import HttpResponseRedirect
from datetime import datetime
from reports.forms import DriveForm, LoginForm, StudentForm, InstructorForm
from .serializers import StudentSerializer
from .models import Student, Instructor, Drive, DriveEvent
from rest_framework import viewsets


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer


class DriveViewSet(viewsets.ModelViewSet):
    queryset = Drive.objects.all()
    serializer_class = DriveSerializer


class DriveEventViewSet(viewsets.ModelViewSet):
    queryset = DriveEvent.objects.all()
    serializer_class = DriveSerializer


def home(request):
    return render(request, 'index.html', {})


def login(request):
    form = LoginForm
    context = {'form': form}
    return render(request, 'login.html', context)


def display(request):
    pass


def create_drive(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        student = form.save(commit=False)
        student.save()

        return HttpResponseRedirect(student.absolute_url())

    context = {'form': form}
    return render(request, 'drive_form.html', context)


def create_student():
    form = StudentForm(request.POST or None)
    if form.is_valid():
        student = form.save(commit=False)
        student.updated = datetime.now()
        student.save()

        return HttpResponseRedirect(student.absolute_url())

    context = {'form': form}
    return render(request, 'student_form.html', context)


def create_instructor():
    form = InstructorForm(request.POST or None)
    if form.is_valid():
        instructor = form.save(commit=False)
        instructor.updated = datetime.now()
        instructor.save()

        return HttpResponseRedirect(instructor.absolute_url())

    context = {'form': form}
    return render(request, 'instructor_form.html', context)


def drive_detail(request):
    pass


def update_drive(request):
    pass


def delete_drive(request):
    pass


def form(request):
    return render(request, 'form.html', {})


def form_advanced(request):
    return render(request, 'form_advanced.html', {})


def form_validation(request):
    return render(request, 'form_validation.html', {})


def form_wizard(request):
    return render(request, 'form_wizard.html', {})


def form_upload(request):
    return render(request, 'form_upload.html', {})


def form_buttons(request):
    return render(request, 'form_buttons.html', {})