from rest_framework import serializers
from . import models as Models

class ScheduleSerializer(serializers.ModelSerializer) :
	class Meta :
		model = Models.Schedule
		fields = ('pk','player_id','date_start','date_end','club_id','title')



class PostSerializer(serializers.ModelSerializer) :
	class Meta :
		model = Models.Post_list
		fields = ('pk','post_writer','club_name'\
			,'player_num'\
			,'red_p1_name','red_p2_name','red_p3_name','red_p4_name','red_p5_name','red_p6_name','red_p7_name','red_p8_name'\
			,'blue_p1_name','blue_p2_name','blue_p3_name','blue_p4_name','blue_p5_name','blue_p6_name','blue_p7_name','blue_p8_name'\
			,'match_date','match_time_start','match_time_end'\
			,'match_map1','match_map2','match_map3','match_map4','match_map5','match_map6','match_map7'\
			,'match_map8','match_map9','match_map10','match_map11','match_map12','match_map13','match_map14'\
			,'date','passwd','accept','state','result'\
			,'red_goga_avg','blue_goga_avg','blue_win','red_win')

class PlayerSerializer(serializers.ModelSerializer) :
	class Meta :
		model = Models.Player
		fields = ('player_name','passwd','club_id','win','lose','accept')

class RecordSerializer(serializers.ModelSerializer):
	class Meta :
		model = Models.Record
		fields = ('pk','player_id','club_id','record','maps_id','record_date','match_club')

class ClubSerializer(serializers.ModelSerializer):
	class Meta :
		model = Models.Club
		fields = ('club_name')

