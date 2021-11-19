from rest_framework import serializers
from .models import  Exammarks


class ExammarksSerializer(serializers.ModelSerializer):
	class Meta:
		model = Exammarks
		fields = ('id', 'studentid', 'classroomid', 'science', 'maths', 'english', 'total')