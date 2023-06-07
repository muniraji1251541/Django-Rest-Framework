from rest_framework import serializers
from app.models import *


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Student
        fields='__all__'