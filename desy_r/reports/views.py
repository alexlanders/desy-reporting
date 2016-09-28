from django.shortcuts import render
from django.http import HttpResponseRedirect
from datetime import datetime
from reports.forms import DriveForm, LoginForm, StudentForm, InstructorForm, CourseForm, MemberForm
from .models import Student, Member


def home(request):
    context = {}
    return render(request, 'index.html', context)


def login(request):
    form = LoginForm
    context = {'form': form}
    return render(request, 'login.html', context)


def display(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'students.html', context)


def create_drive(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        student = form.save(commit=False)
        student.save()

        return HttpResponseRedirect(student.absolute_url())

    context = {'form': form}
    return render(request, 'drive_form.html', context)


def create_student(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        student = form.save(commit=False)
        student.updated = datetime.now()
        student.save()

        return HttpResponseRedirect(student.absolute_url())

    context = {'form': form}
    return render(request, 'student_form.html', context)


def create_instructor(request):
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


def student_detail(request, pk=None):
    student = Member.objects.get(id=pk)
    context = {'student':student}
    return render(request, 'student.html', context)

