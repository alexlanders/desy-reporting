from .serializers import StudentSerializer, InstructorSerializer, DriveSerializer, DriveEventSerializer
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
    serializer_class = DriveEventSerializer
