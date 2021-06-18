""" Users serializers"""

#Django REST Framework
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

#models
from django.contrib.auth.models import User
from users.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    """Profile model serializer"""

    class Meta:
        model = Profile
        fields = [ 'age', 'city', 'country','header_img', 'profile_picture','followers', 'likes', 'posts']

class UserSerializer(serializers.ModelSerializer):
    """User serializer"""

    profile = ProfileSerializer(read_only=True)

    class Meta:
        model=User
        fields = ['first_name', 'last_name', 'profile']