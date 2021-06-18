""" Users admin config"""

# Django
from django.contrib import admin

# Models
from django.contrib.auth.models import User
from users.models import Teacher, Student, Subject


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title']
    list_display_links = ['id', 'user']
    list_editable = ['title']
    search_fields = ['user__email',
                     'user__is_staff', 'created_at', 'modified_at']
    list_filter = ['user__is_active',
                   'user__is_staff', 'created_at', 'modified_at']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'student_number', 'group']
    list_display_links = ['id', 'user']
    list_editable = ['group']
    search_fields = ['user__email', 'user__created']
    list_filter = ['user__is_active']


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'short_name', 'full_name', 'teacher']
    list_display_links = ['id']
    search_fields = ['short_name']
    list_filter = ['teacher']
