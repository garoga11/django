
from django.contrib import admin
from django.contrib.auth import logout
from django.shortcuts import resolve_url
from django.urls import path
from users import views as users_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', users_views.login_view, name='login'),
    path('new/', users_views.signup, name="signup"),
    path('landing/', users_views.landing, name='landing'),
    path('logout/', users_views.logout_view, name='logout'),
    path('update/profile', users_views.update_teacher_profile, name='update_teacher_profile'),
    path('update/profile/students', users_views.update_student_profile, name='update_student_profile')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
