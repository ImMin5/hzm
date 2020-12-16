from rest_framework import serializers
from . import models as Models

class ScheduleSerializer(serializers.ModelSerializer) :
	class Meta :
		model = Models.Schedule
		fields = ('pk','player_id','date_start','date_end','club_id','title')



class MatchSerializer(serializers.ModelSerializer) :
	class Meta :
		model = Models.Match
		fields = ('pk','red_club_id','red_club_name','blue_club_id','blue_club_name','post_writer'\
			,'player_num'\
			,'red_player_name','blue_player_name'\
			,'match_date','match_time_start','match_time_end'\
			,'match_map'\
			,'date','passwd','accept','state','result'\
			,'red_goga_avg','blue_goga_avg','blue_win','red_win')

class PlayerSerializer(serializers.ModelSerializer) :
	class Meta :
		model = Models.Player
		fields = ('player_name','passwd','club_id','win','lose','accept')

class RecordSerializer(serializers.ModelSerializer):
	class Meta :
		model = Models.Record
		fields = ('pk','player_id','club_id','record','maps_id','map_name','record_date','match_club')

class ClubSerializer(serializers.ModelSerializer):
	class Meta :
		model = Models.Club
		fields = ('club_name','description')

