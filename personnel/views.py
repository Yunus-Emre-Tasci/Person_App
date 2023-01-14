from django.shortcuts import render
from .serializers import DepartmentSerializer,PersonnelSerializer
from rest_framework import generics,status
from .models import Department,Personnel
from .permissions import IsStafforReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.

class DepartmentView(generics.ListCreateAPIView):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer
    permission_classes=[IsStafforReadOnly,IsAuthenticated]
    

class PersonnelListCreateView(generics.ListCreateAPIView):
    queryset=Personnel.objects.all()
    serializer_class=PersonnelSerializer   
    # permission_classes=[IsAuthenticated,IsStafforReadOnly] 
    permission_classes=[IsAuthenticated] 
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if self.request.user.is_staff:
            personnel=self.perform_create(serializer)
            data={
                "message":f"Personal {personnel.first_name} saved successfully",
                "personnel":serializer.data
            }
        else:
            data={
                "message":"You are not authorized to perform this operation"
            }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)
              
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_create(self, serializer):
        serializer.save()