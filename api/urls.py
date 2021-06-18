from django.contrib import admin
from django.urls import path

#static files config
from django.conf import settings
from django.conf.urls.static import static

from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', users_views.list_users),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
