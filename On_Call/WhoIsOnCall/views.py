from django.shortcuts import render

from django.shortcuts import render
from rest_framework import viewsets
from .serializers import OrganisationSerializer, ProfileSerializer
from .models import Organisation, Profile


class OrganisationView(viewsets.ModelViewSet):
    serializer_class = OrganisationSerializer
    queryset = Organisation.objects.all()


class ProfileView(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()