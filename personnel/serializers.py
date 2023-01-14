from rest_framework import serializers
from .models import Department,Personnel

class DepartmentSerializer(serializers.ModelSerializer):
    
    personnel_count=serializers.SerializerMethodField()
    
    class Meta:
        model=Department
        fields=("id","name","personnel_count")
        
    def get_personnel_count(self,obj):
        return obj.personals.count()    
    

class PersonnelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Personnel
        fields="__all__"    