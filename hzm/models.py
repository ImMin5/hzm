from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.
#PLAYER
SIZE_PLAYER_NAME = 12
SIZE_PLAYER_PASSWORD = 21

#MAP
SIZE_MAP_NAME = 30

#CLUB
SIZE_CLUB_NAME = 12

#RECORD
SIZE_RECORD = 8

#SCHEDULE
SIZE_TITLE = 30
#MATCH 
SIZE_STATE =4

#FREEBOARD
SIZE_FREEBOARD_DESCRIPTION=1000
SIZE_POST_COMMENT=200


#공통
SIZE_POST_TITLE=20
SIZE_DATE = 10
SIZE_TIME = 11
SIZE_DATE_TIME = 22
SIZE_DESCRIPTION =300


class Player(models.Model):
	player_name = models.CharField(max_length=SIZE_PLAYER_NAME, blank=True, null= True)
	passwd = models.CharField(max_length=SIZE_PLAYER_PASSWORD, blank=True, null= True)
	club = models.ForeignKey('Club', on_delete=models.SET_NULL, blank=True, null=True)
	win = models.IntegerField(default=0,blank=True, null= True)
	lose = models.IntegerField(default=0,blank=True, null= True)
	accept = models.BooleanField(default=False)	
	date = models.CharField(max_length=SIZE_DATE, blank=True, null= True)

class Record(models.Model):
	player = models.ForeignKey('Player', on_delete=models.CASCADE, blank=True, null=True)
	maps = models.ForeignKey('Map',on_delete=models.CASCADE,blank=True,null=True)
	map_name = models.CharField(max_length=SIZE_MAP_NAME,blank=True, null=True)
	club= models.ForeignKey('Club', on_delete=models.CASCADE, blank=True, null=True)
	record = models.CharField(max_length=SIZE_RECORD,blank=True, null=True)
	record_date = models.CharField(max_length=SIZE_DATE,blank=True, null=True)
	match_club = models.CharField(max_length=SIZE_CLUB_NAME,blank=True, null=True)

class Map(models.Model):
	map_name = models.CharField(max_length=30, blank=True, null= True)
	date = models.CharField(max_length=10,blank=True, null=True)

class Match(models.Model):
	red_club_id = models.IntegerField(blank=True, null= True)
	red_club_name = models.CharField(max_length=SIZE_CLUB_NAME, blank=True, null= True)
	blue_club_id = models.IntegerField(blank=True, null= True)
	blue_club_name = models.CharField(max_length=SIZE_CLUB_NAME, blank=True, null= True)
	post_writer = models.CharField(max_length=SIZE_PLAYER_NAME, blank=True, null= True)
	passwd = models.CharField(max_length=SIZE_PLAYER_PASSWORD, blank=True, null= True)
	player_num = models.IntegerField(default=2,blank=True, null= True)
	red_player_name = ArrayField(models.CharField(max_length=SIZE_PLAYER_NAME, blank=True, null= True), blank=True, null= True)
	red_player_id = ArrayField(models.IntegerField(default=0, blank=True, null= True), blank=True, null= True)
	blue_player_name = ArrayField(models.CharField(max_length=SIZE_PLAYER_NAME, blank=True, null= True), blank=True, null= True)
	blue_player_id = ArrayField(models.IntegerField(default=0, blank=True, null= True), blank=True, null= True)
	match_date = models.CharField(max_length=SIZE_DATE, blank=True, null= True)
	match_time_start = models.CharField(max_length=SIZE_TIME,blank=True, null=True)
	match_time_end = models.CharField(max_length=SIZE_TIME,blank=True, null=True)
	match_map = ArrayField(models.CharField(max_length=SIZE_MAP_NAME, blank=True, null= True), blank = True, null= True)
	date = models.CharField(max_length=SIZE_DATE_TIME, blank=True, null= True)
	red_goga_avg = models.CharField(max_length=SIZE_RECORD, blank=True, null= True)
	blue_goga_avg = models.CharField(max_length=SIZE_RECORD, blank=True, null= True)
	accept = models.BooleanField(default=False)
	state = models.CharField(max_length=SIZE_STATE, blank=True, null= True)
	result = models.BooleanField(default=False)
	red_win = models.IntegerField(default=0,blank=True, null= True)
	blue_win = models.IntegerField(default=0,blank=True, null= True)

class Schedule(models.Model):
	player = models.ForeignKey('Player', on_delete=models.CASCADE, blank=True, null=True)
	club = models.ForeignKey('Club', on_delete=models.CASCADE, blank=True, null=True)
	title = models.CharField(max_length=128,blank=True, null=True)
	date_start = models.CharField(max_length=SIZE_DATE_TIME, blank=True, null= True)
	date_end = models.CharField(max_length=SIZE_DATE_TIME, blank=True, null= True)

class Matchresult(models.Model):
	match=models.ForeignKey('Match', on_delete=models.SET_NULL, blank=True, null=True)
	player=models.ForeignKey('Player', on_delete=models.SET_NULL, blank=True, null=True)
	result = models.BooleanField(default=False)
	club_name =models.CharField(max_length=SIZE_CLUB_NAME, blank=True, null= True)

class Club(models.Model) :
	club_name=models.CharField(max_length=SIZE_CLUB_NAME, blank=True, null= True)
	host=models.CharField(max_length=SIZE_PLAYER_NAME, blank=True, null= True)
	description=models.TextField(max_length=SIZE_DESCRIPTION, blank=True, null= True)
	member = models.IntegerField(default=0, blank=True, null=True)


class Matchred(models.Model) :
	club=models.ForeignKey('Club', on_delete=models.SET_NULL, blank=True, null=True)
	post_writer = models.CharField(max_length=SIZE_PLAYER_NAME, blank=True, null= True)
	player_name = ArrayField(models.CharField(max_length=SIZE_PLAYER_NAME,blank=True, null=True))
	player_id = ArrayField(models.IntegerField(default=0, blank=True, null = True))

class Freeboard(models.Model) :
	player=models.ForeignKey('Player', on_delete=models.SET_NULL, blank=True, null=True)
	club=models.ForeignKey('Club', on_delete=models.SET_NULL, blank=True, null=True)
	post_writer=models.CharField(max_length=SIZE_PLAYER_NAME, blank=True, null= True)
	title = models.CharField(max_length=SIZE_POST_TITLE, blank=True, null= True)
	date=models.CharField(max_length=SIZE_DATE_TIME, blank=True, null= True)
	view = models.IntegerField(default=0, blank=True, null=True)
	description=models.TextField(max_length=SIZE_FREEBOARD_DESCRIPTION, blank=True, null= True)
	notice=models.BooleanField(default=False)
	comment_count=models.IntegerField(default=0,blank=True, null= True)

class Freeboardcomment(models.Model) :
	player=models.ForeignKey('Player', on_delete=models.SET_NULL, blank=True, null=True)
	post=models.ForeignKey('Freeboard', on_delete=models.SET_NULL, blank=True, null=True)
	player_name = models.CharField(max_length=SIZE_PLAYER_NAME, blank=True, null= True)
	date=models.CharField(max_length=SIZE_DATE_TIME, blank=True, null= True)
	comments=models.CharField(max_length=SIZE_POST_COMMENT,blank=True, null = True)