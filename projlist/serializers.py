from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = '__all__'
        
    def create(self, validated_data):
        validated_data['content'] = '\\n'.join(validated_data['content'].split('\n'))
        return Project.objects.create(**validated_data)
        

# Create your models here.
