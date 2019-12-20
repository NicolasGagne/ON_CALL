"""
Contain all the Serialiser for the App
"""

from rest_framework import serializers
from .models import Organisation

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = ('id', 'name', 'description', 'private')