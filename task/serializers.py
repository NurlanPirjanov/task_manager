from rest_framework import serializers
from .models import TaskManager
class TaskAPIListSerializer(serializers.ModelSerializer):
	class Meta:
		model = TaskManager
		fields = '__all__'