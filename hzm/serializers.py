from rest_framework import serializers
from . import models as Models

class ScheduleSerializer(serializers.ModelSerializer) :
	class Meta :
		model = Models.Schedule
		fields = ('pk','player','date_start','date_end','club_name','title')



class PostSerializer(serializers.ModelSerializer) :
	class Meta :
		model = Models.Post_list
		fields = ('pk','post_writer','club_name'\
			,'player_num'\
			,'player1_name','player2_name','player3_name','player4_name','player5_name','player6_name','player7_name','player8_name'\
			,'match_date','match_time_start','match_time_end'\
			,'match_map1','match_map2','match_map3','match_map4','match_map5','match_map6','match_map7'\
			,'match_map8','match_map9','match_map10','match_map11','match_map12','match_map13','match_map14'\
			,'date','post_passwd')



