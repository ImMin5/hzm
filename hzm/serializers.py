from rest_framework import serializers
from . import models as Models

class ScheduleSerializer(serializers.ModelSerializer) :
	class Meta :
		model = Models.Schedule
		fields = ('player','date_start','date_end','club_name','title')


