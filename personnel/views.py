from django.shortcuts import render
from .serializers import DepartmentSerializer,PersonnelSerializer
from rest_framework import generics
from .models import Department,Personnel
from .permissions import IsStafforReadOnly
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class DepartmentView(generics.ListCreateAPIView):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer
    permission_classes=[IsStafforReadOnly,IsAuthenticated]
    

class PersonnelListCreateView(generics.ListCreateAPIView):
    queryset=Personnel.objects.all()
    serializer_class=PersonnelSerializer    