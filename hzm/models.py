from django.db import models

# Create your models here.


class Player(models.Model):
	player_id = models.CharField(max_length=128, blank=True, null=True)
	player_passwd = models.CharField(max_length=128, blank=True, null= True)
	club_name = models.CharField(max_length=128,blank=True, null=True)

class Record(models.Model):
	player = models.ForeignKey('Player', on_delete=models.SET_NULL, blank=True, null=True)
	club_name = models.CharField(max_length=128,blank=True, null= True)
	record = models.TimeField()
	map_name = models.ForeignKey('Map',on_delete=models.SET_NULL,null=True)
	match_data = models.DateField()
	match_club = models.CharField(max_length=128,blank=True, null=True)

class Map(models.Model):
	map_name = models.CharField(max_length=128,blank=True, null=True)
	map_test_record = models.TimeField()

class Post_list(models.Model):
	club_name = models.CharField(max_length=128, blank=True, null= True)
	post_writer = models.CharField(max_length=128, blank=True, null= True)
	player_num = models.IntegerField(default=4,blank=True, null= True)
	player1_name = models.CharField(max_length=128, blank=True, null= True)
	player2_name = models.CharField(max_length=128, blank=True, null= True)
	player3_name = models.CharField(max_length=128, blank=True, null= True)
	player4_name = models.CharField(max_length=128, blank=True, null= True)
	player5_name = models.CharField(max_length=128, blank=True, null= True)
	player6_name = models.CharField(max_length=128, blank=True, null= True)
	player7_name = models.CharField(max_length=128, blank=True, null= True)
	player8_name = models.CharField(max_length=128, blank=True, null= True)
	match_date = models.CharField(max_length=128, blank=True, null= True)
	match_time_start = models.TimeField(blank=True, null= True)
	match_time_end = models.TimeField(blank=True, null= True)
	post_passwd = models.CharField(max_length=128, blank=True, null= True)
	match_map1 = models.CharField(max_length=128, blank=True, null= True)
	match_map2 = models.CharField(max_length=128, blank=True, null= True)
	match_map3 = models.CharField(max_length=128, blank=True, null= True)
	match_map4 = models.CharField(max_length=128, blank=True, null= True)
	match_map5 = models.CharField(max_length=128, blank=True, null= True)
	match_map6 = models.CharField(max_length=128, blank=True, null= True)
	match_map7 = models.CharField(max_length=128, blank=True, null= True)
	match_map8 = models.CharField(max_length=128, blank=True, null= True)
	match_map9 = models.CharField(max_length=128, blank=True, null= True)
	match_map10 = models.CharField(max_length=128, blank=True, null= True)
	match_map11 = models.CharField(max_length=128, blank=True, null= True)
	match_map12 = models.CharField(max_length=128, blank=True, null= True)
	match_map13 = models.CharField(max_length=128, blank=True, null= True)
	match_map14 = models.CharField(max_length=128, blank=True, null= True)






