from django.shortcuts import render
from django.http import HttpResponseRedirect
from datetime import datetime
from reports.forms import DriveForm, LoginForm, StudentForm, InstructorForm


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
    form = DriveForm(request.POST or None)
    if form.is_valid():
        drive = form.save(commit=False)
        drive.updated = datetime.now()
        drive.save()

        return HttpResponseRedirect(drive.absolute_url())

    context = {'form': form}
    return render(request, 'drive_form.html', context)

def create_instructor():
    pass

def drive_detail(request):
    pass

def update_drive(request):
    pass

def delete_drive(request):
    pass