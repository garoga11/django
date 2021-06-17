""" Complete profile middleare"""

from django.shortcuts import render, redirect
from django.urls import reverse

class ProfileCompletionMiddleware:
    """Ensure every user that is interacting in the platform have a complete profile"""

    def __init__(self, get_response):
        """Initialization"""
        
        self.get_response = get_response


    def __call__(self, request):
        """Code to be executed for each request before the view is called"""
        
        if not request.user.is_staff and not request.user.is_anonymous:
            try:
                profile = request.user.teacher
            
            except:
                pass
            try:
                profile = request.user.student
            except:
                pass

            if profile.type_of_user == "teacher":
                if not profile.title:
                    if request.path not in [reverse('update_teacher_profile'), reverse('logout')]:
                        return redirect('update_teacher_profile')

            elif profile.type_of_user == "student":
                if not profile.student_number or not profile.subject or not profile.group or not profile.career:
                    if request.path not in [reverse('update_student_profile'), reverse('logout')]:
                        return redirect('update_student_profile')
        response = self.get_response(request)
        return response
