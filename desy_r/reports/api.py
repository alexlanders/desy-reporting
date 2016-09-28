from .serializers import MemberSerializer, StudentSerializer, InstructorSerializer, DriveSerializer, ObjectiveSerializer, CourseSerializer
from .models import Member, Student, Instructor, Drive, Objective, Course
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


class ObjectiveViewSet(viewsets.ModelViewSet):
    queryset = Objective.objects.all()
    serializer_class = ObjectiveSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
