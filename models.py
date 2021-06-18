""" Users Models"""
# Django

from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    type_of_user = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title', 'created_at']

    def __str__(self):
        return self.user.get_full_name()


class Subject(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=CASCADE)
    short_name = models.CharField(max_length=10, blank=True)
    full_name = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ['short_name']

    def __str__(self):
        return self.short_name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_number = models.CharField(max_length=100, blank=True)
    type_of_user = models.CharField(max_length=100, blank=True)
    subject = models.ManyToManyField(Subject)
    group = models.CharField(max_length=100, blank=True)

    CAREERS = [
        ("TI", "TI"),
        ("DN", "DN"),
        ("PI", "PI")
    ]

    career = models.CharField(choices=CAREERS, max_length=50)

    class Meta:
        ordering = ['group', 'career', 'student_number']

    def __str__(self):
        return self.user.get_full_name()
# Create your models here.
