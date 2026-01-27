from rest_framework import serializers
from myapp.models import *

class student_Serialize(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'