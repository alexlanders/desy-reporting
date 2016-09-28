from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Student, Instructor, Drive, Objective, Course, Member


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = ('user', 'lenses', 'permit')


class InstructorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Instructor
        fields = ('user', 'instructor_id')


class DriveSerializer(serializers.ModelSerializer):
    student, instructor = StudentSerializer(), InstructorSerializer()

    class Meta:
        model = Drive
        fields = '__all__'


class ObjectiveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Objective
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = '__all__'