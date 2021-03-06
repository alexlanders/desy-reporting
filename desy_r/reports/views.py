from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from itertools import islice
from datetime import datetime
from reports.forms import DriveForm, LoginForm, StudentForm, InstructorForm, CourseForm, MemberForm
from .models import Student, Member, Course, Drive


def home(request):
    context = {}
    return render(request, 'index.html', context)


def login(request):
    form = LoginForm
    context = {'form': form}
    return render(request, 'login.html', context)


def all_classes(request):
    class_query = Course.objects.all()
    paginator = Paginator(class_query, 25)
    page = request.GET.get('page')
    try:
        # One page worth of students
        classes = paginator.page(page)
        class_range = list(paginator.page_range)[int(page):int(page) + 5]
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        classes = paginator.page(1)
        class_range = list(paginator.page_range)[0:5]

    context = {'classes': classes, 'class_range': list(class_range)}
    return render(request, 'all_classes.html', context)


def current_classes(request):
    class_query = Course.objects.all()
    paginator = Paginator(class_query, 25)
    page = request.GET.get('page')
    try:
        # One page worth of students
        classes = paginator.page(page)
        class_range = list(paginator.page_range)[int(page):int(page) + 5]
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        classes = paginator.page(1)
        class_range = list(paginator.page_range)[0:5]

    context = {'classes': classes, 'class_range': list(class_range)}
    return render(request, 'current_classes.html', context)


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

    student_list = ["{}".format(student) for student in student_query]
    student_id_list = ["{}".format(student.user.id) for student in student_query]

    context = {'students': students, 'student_range': list(student_range), 'student_list': student_list,
               'student_id_list': student_id_list}
    return render(request, 'students.html', context)


def current_students(request):
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

    context = {'students': students, 'student_range': list(student_range)}
    return render(request, 'current_students.html', context)


def create_drive(request):
    form = DriveForm(request.POST or None)
    if form.is_valid():
        student = form.save(commit=False)
        student.save()

        return HttpResponseRedirect(student.absolute_url())

    context = {'form': form}
    return render(request, 'create_drive.html', context)


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
    recent_drives = student.drives.order_by('-date')
    last_date = recent_drives.last().date.strftime("%B %d, %Y")
    first_date = recent_drives.first().date.strftime("%B %d, %Y")
    drive_hours = ((student.total_hours_driven/6.75)*100)
    observed_hours = ((student.total_hours_observed/10)*100)
    context = {'student': student, 'last_date': last_date, 'first_date': first_date, 'recent_drives': recent_drives,
               'drive_hours': drive_hours, 'observed_hours': observed_hours}

    return render(request, 'student.html', context)


def class_detail(request, pk=None):
    klass = Course.objects.get(id=pk)
    students = klass.students.all()
    drives = Drive.objects.all()

    scores = [drive.score for student in students for drive in student.drives.all()]
    avg_drive_score = sum(scores) // len(scores)

    number_of_students = students.count()

    context = {'klass': klass, 'students': students, 'number_of_students': number_of_students, 'drives': drives,
               'avg_drive_score': avg_drive_score}
    return render(request, 'class_detail.html', context)


def calendar_page(request):
    class_query = Course.objects.order_by('-end_date')
    paginator = Paginator(class_query, 25)
    page = request.GET.get('page')
    try:
        # One page worth of classes
        classes = paginator.page(page)
        class_range = list(paginator.page_range)[int(page):int(page) + 5]
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        classes = paginator.page(1)
        class_range = list(paginator.page_range)[0:5]

    drives = Drive.objects.all()

    context = {'classes': classes, 'class_range': list(class_range), 'drives': drives}
    return render(request, 'calendar.html', context)
