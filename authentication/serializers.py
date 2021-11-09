from rest_framework import serializers
from .models import Students, Exammarks


class ExammarksSerializer(serializers.ModelSerializer):
	studentname = serializers.CharField(source='studentid.student_name')

	class Meta:
		model = Exammarks
		fields = ('studentid', 'classroomid', 'total')





