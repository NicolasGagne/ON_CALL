from django.shortcuts import render

from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Organisation


class OrganisationView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Organisation.objects.all()