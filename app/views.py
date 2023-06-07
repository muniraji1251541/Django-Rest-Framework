from django.shortcuts import render
from app.models import *
from app.serializers import *
from rest_framework import viewsets

# Create your views here.

class StudentViews(viewsets.ModelViewSet):
    serializer_class=StudentSerializer
    queryset=Student.objects.all()