from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from itertools import islice
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


def all_students(request):
    student_query = Student.objects.all()
    paginator = Paginator(student_query, 25)

    page = request.GET.get('page')
    try:
        # One page worth of students
        students = paginator.page(page)
        student_range = list(paginator.page_range)[int(page):int(page)+5]
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        students = paginator.page(1)
        student_range = list(paginator.page_range)[0:5]

    print(list(student_range))
    context = {'students': students, 'student_range': list(student_range)}
    return render(request, 'students.html', context)


def create_drive(request):
    form = DriveForm(request.POST or None)
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


def display(request):
    return render(request, 'index.html', {})


def student_detail(request, pk=None):
    student = Student.objects.get(id=pk)
    recent_drives = student.drives.all()
    drive_hours = ((student.total_hours_driven/6.75)*100)
    observed_hours = ((student.total_hours_observed/10)*100)
    context = {'student': student, 'recent_drives': recent_drives, 'drive_hours': drive_hours, 'observed_hours': observed_hours}
    return render(request, 'student.html', context)


def calendar_page(request):
    context = {}
    return render(request, 'calendar.html', context)

