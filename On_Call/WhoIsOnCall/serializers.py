"""
Contain all the Serialiser for the App
"""

from rest_framework import serializers
from .models import Organisation, Profile
from django.contrib.auth.models import User

class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = ('id', 'name', 'description', 'private')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', "last_name", "email", )


class ProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ("user", 'bio', 'location', 'birth_date', "occupation")