from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Player(models.Model):
	player_name = models.CharField(max_length=128, blank=True, null=True)
	passwd = models.CharField(max_length=128, blank=True, null= True)
	club_name = models.CharField(max_length=128,blank=True, null=True)
	win = models.IntegerField(default=0,blank=True, null= True)
	lose = models.IntegerField(default=0,blank=True, null= True)

class Record(models.Model):
	player = models.ForeignKey('Player', on_delete=models.SET_NULL, blank=True, null=True)
	club_name = models.CharField(max_length=128,blank=True, null= True)
	record = models.TimeField()
	map_name = models.ForeignKey('Map',on_delete=models.SET_NULL,null=True)
	match_date = models.DateField()
	match_club = models.CharField(max_length=128,blank=True, null=True)

class Map(models.Model):
	map_name = models.CharField(max_length=128,blank=True, null=True)
	map_test_record = models.TimeField()

class Post_list(models.Model):
	club_name = models.CharField(max_length=128, blank=True, null= True)
	post_writer = models.CharField(max_length=128, blank=True, null= True)
	player_num = models.IntegerField(default=2,blank=True, null= True)
	red_p1_name = models.CharField(max_length=128, blank=True, null= True)
	red_p2_name = models.CharField(max_length=128, blank=True, null= True)
	red_p3_name = models.CharField(max_length=128, blank=True, null= True)
	red_p4_name = models.CharField(max_length=128, blank=True, null= True)
	red_p5_name = models.CharField(max_length=128, blank=True, null= True)
	red_p6_name = models.CharField(max_length=128, blank=True, null= True)
	red_p7_name = models.CharField(max_length=128, blank=True, null= True)
	red_p8_name = models.CharField(max_length=128, blank=True, null= True)
	blue_p1_name = models.CharField(max_length=128, blank=True, null= True)
	blue_p2_name = models.CharField(max_length=128, blank=True, null= True)
	blue_p3_name = models.CharField(max_length=128, blank=True, null= True)
	blue_p4_name = models.CharField(max_length=128, blank=True, null= True)
	blue_p5_name = models.CharField(max_length=128, blank=True, null= True)
	blue_p6_name = models.CharField(max_length=128, blank=True, null= True)
	blue_p7_name = models.CharField(max_length=128, blank=True, null= True)
	blue_p8_name = models.CharField(max_length=128, blank=True, null= True)
	match_date = models.CharField(max_length=128, blank=True, null= True)
	match_date = models.CharField(max_length=128, blank=True, null= True)
	match_time_start = models.CharField(max_length=128,blank=True, null=True)
	match_time_end = models.CharField(max_length=128,blank=True, null=True)
	passwd = models.CharField(max_length=128, blank=True, null= True)
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
	date = models.CharField(max_length=128, blank=True, null= True)
	red_goga_avg = models.CharField(max_length=128, blank=True, null= True)
	blue_goga_avg = models.CharField(max_length=128, blank=True, null= True)
	state = models.BooleanField(default=False) 
	result = models.BooleanField(default=False)
	blue_win = models.IntegerField(default=0,blank=True, null= True)
	red_win = models.IntegerField(default=0,blank=True, null= True)
	
class Schedule(models.Model):
	player = models.ForeignKey('Player', on_delete=models.SET_NULL, blank=True, null=True)
	club_name = models.CharField(max_length=128,blank=True, null=True)
	title = models.CharField(max_length=128,blank=True, null=True)
	date_start = models.CharField(max_length=128, blank=True, null= True)
	date_end = models.CharField(max_length=128, blank=True, null= True)



