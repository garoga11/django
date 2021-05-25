""" Users admin config"""

# Django
from django.contrib import admin

# Models
from django.contrib.auth.models import User
from user.models import Teacher, Student, Subject


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'teacher', 'title']
    list_display_links = ['id', 'teacher']
    list_editable = ['title']
    search_fields = ['teacher__email',
                     'teacher__is_staff', 'created_at', 'modified_at']
    list_filter = ['teacher__email',
                   'teacher__is_staff', 'created_at', 'modified_at']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'student_number', 'gruop']
    list_display_links = ['id', 'student']
    list_editable = ['group']
    search_fields = ['student_email', 'student__created']
    list_filter = ['student__is_active']


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'short_name', 'full_name', 'teacher']
    list_display_links = ['id']
    search_fields = ['short_name']
    list_filter = ['teacher']
