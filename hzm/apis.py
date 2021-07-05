from django.http import JsonResponse, HttpResponse, FileResponse, HttpResponseRedirect
from django.urls import reverse
from hzm.models import *
import requests
import json
import os
from django.utils import timezone
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.files.storage import default_storage #파일 저장 경로
from django.conf import settings
from django.db.models import Q
from .serializers import *
import time
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.db.models import Count,Max,Min
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
from hzm.logs import *
import logging

log_dir = create_dir()

my_club = "학지매"
master_passwd = "ssdsmh"
club_passwd ="hzm"

def id_check_btn (request) :
	player_name = request.GET.get('player_name')
	
	try :
		check_id = Player.objects.get(player_name=player_name)
		print(check_id)
		if check_id is not None :
			return HttpResponse("fail")
		else :
			return HttpResponse("good") 

	except Exception as e :
		return HttpResponse("good")


def id_check (request) :
	player_name = request.GET.get('player_id')

	try :
		check_id = Player.objects.get(player_name=player_name)
		return HttpResponse("fail")
	except Exception as e :
		return HttpResponse("good")

def edit_mypage_info(request) :
	pk=request.session.get('pk')
	player_name=request.session.get('player_name')
	name=request.POST.get('player_name')
	password_now=request.POST.get('password_now')
	password_change=request.POST.get('password_change')
	p = Player.objects.filter(player_name=name).exclude(player_name=player_name)
	
	if p.exists() :
		data={'msg':'sameId'}
		return HttpResponse(data)

	try:
		player=Player.objects.get(pk=pk)
		club=Club.objects.get(pk=player.club_id)

		#비밀번호가 일치할 경우
		if player.passwd == password_now :
			#클럽장이 이름을 바꿀 경우
			if club.host == player.player_name :
				club.host = name
				club.save()
			#일반 라이더가 이름을 바꿀 경우
			if player.player_name != name :
				player.player_name = name
				player.save()
			#비밀번호를 변경할 경우
			if password_change :
				log_start(request,log_dir+'/'+str(player.pk)+'.log',"changed password : "+password_change)
				player.passwd = password_change
				player.save()
			
			#세션에 바뀐 이름으로 넣어줌
			request.session['player_name'] = name
			log_start(request,log_dir+'/'+str(player.pk)+'.log',"changed player_name "+name)
			data = {
				'msg' : 'good',
				'player_name' : name,
			}
			return JsonResponse(data)
		else :
			data = {
				'msg' : 'passwordfail',
			}
			return JsonResponse(data)
	except Exception as e :
		data = {
				'msg' : 'fail',
			}
		print(e)
		return JsonResponse(data)

def sign_in(request) :
	player_name = request.POST.get('player_name')
	player_passwd = request.POST.get('player_passwd')
	try :
		if request.method == 'POST' :
			player = Player.objects.get(Q(player_name=player_name) & Q(passwd=player_passwd))
			data = {}
			if player.accept == False :
				return HttpResponse("auth_fail")
			if player.player_name is not None:
				request.session['pk'] = player.pk
				request.session['player_name'] = player.player_name
				request.session['club_id'] = player.club.pk
				log_start(request,log_dir+'/'+str(player.pk)+'.log',player.player_name+" login")
				return HttpResponse("login")
			else :
				print('NONE')
				return HttpResponse('login_fail1')
		else :
			return HttpResponse('login_fail2')
	except Exception as e :
		return HttpResponse("login_fail3")


def sign_up(request) :
	player_name = request.POST.get('player_name')
	player_password = request.POST.get('player_password')
	club_name = request.POST.get('club_name')
	club = Club.objects.get(club_name=club_name)
	try :
		if request.method == 'POST' :
			print('POST')
			print(player_name)
			player = Player(player_name=player_name, passwd=player_password, club_id=club.pk)
			player.save()
			return redirect('/')
		else :
			return redirect('/')
	except Exception as e : 
		print(e)
		print('create id error')
		return HttpResponse(e)

def logout(request) :
	try :
		pk=request.session.get('pk')
		player=Player.objects.get(pk=pk)
		log_start(request,log_dir+'/'+str(player.pk)+'.log',player.player_name+" logout")
		request.session.clear()
		return HttpResponse("good")
	except Exception as e :
		print(e)
		return redirect('hzm:error_page')


def add_fmatch(request) :
	try :
		post_writer = request.POST.get('post_writer')
		red_club_name = request.POST.get('club_red')
		blue_club_name = request.POST.get('club_blue')
		match_date = request.POST.get('match_date')
		match_time_start = request.POST.get('match_time_start')
		match_time_end = request.POST.get('match_time_end')
		player_num = request.POST.get('player_num')
		passwd = request.POST.get('passwd')
		blue_goga_avg = request.POST.get('blue_goga_avg')
		date = request.POST.get('date')
		player= request.POST.get('player[]')
		players_= player.split(',')
		club=Club.objects.get(club_name=red_club_name)
		match = Match(post_writer=post_writer,red_club_id=club.pk,red_club_name=club.club_name ,blue_club_name=blue_club_name,\
		player_num=player_num, blue_player_name=players_,\
		match_date=match_date, match_time_start=match_time_start, match_time_end=match_time_end,\
		passwd=passwd,blue_goga_avg=blue_goga_avg,date=date)
		pr
		match.save()
		log_start(request,log_dir+'/today.log',post_writer+" submit fmatch :"+str(match.pk))
		return redirect('/')
	except Exception as e :
		print(e)
		return redirect('/')

def add_schedule(request) :
	pk = request.session['pk']
	player = Player.objects.get(pk=pk)
	title = request.POST.get('title')
	date_start = request.POST.get('date_start')
	date_end =request.POST.get('date_end')

	schedule = Schedule(player_id=pk,date_start=date_start,date_end=date_end,title=title)
	schedule.save()

	data = {
		'title' : schedule.title,
		'date_end' : schedule.date_end,
		'date_start' : schedule.date_start,
		'pk' : schedule.pk,
	}
	log_start(request,log_dir+'/'+str(player.pk)+'.log',player.player_name+" made schedule : "+str(schdule.pk))
	return JsonResponse(data)

def get_my_schedules(request) :

	pk = request.session['pk']
	schedules = Schedule.objects.filter(player_id=pk)
	serialized_schedules = ScheduleSerializer(schedules,many=True)

	return HttpResponse(json.dumps(serialized_schedules.data))

def create_my_schedule_table(request) :

	now = time.localtime()

	mon = str(now.tm_mon)
	day = str(now.tm_mday)
	hour=str(now.tm_hour)
	mins=str(now.tm_min)
	sec=str(now.tm_sec)


	if now.tm_mon < 10 :
		mon= str('0')+str(now.tm_mon)
	if now.tm_mday < 10 :
		day= str('0')+str(now.tm_mday)
	if now.tm_hour < 10 :
		hour= str('0')+str(now.tm_hour)
	if now.tm_min < 10 :
		hour= str('0')+str(now.tm_min)
	if now.tm_sec < 10 :
		sec= str('0')+str(now.tm_sec)


	date_now = str(now.tm_year)+'-'+mon\
	+'-'+day+'T'+hour+':'+mins+':'+sec

	pk = request.session['pk']
	schedules = Schedule.objects.filter(Q(player_id=pk) & Q(date_start__gte=date_now)).order_by('date_start')
	serialized_schedules = ScheduleSerializer(schedules,many=True)

	return HttpResponse(json.dumps(serialized_schedules.data))



def get_all_schedules(request) :
	pk = request.session['pk']
	try :
		player=Player.objects.get(pk=pk)
		schedules = Schedule.objects.filter(club_id=player.club_id).exclude(player_id=player.pk)
		serialized_schedules = ScheduleSerializer(schedules,many=True)
		return HttpResponse(json.dumps(serialized_schedules.data))
	except Exception as e :
		return redirect('/')

def delete_my_schedule(request) :
	try :
		pk=requset.session.get('pk')
		s_pk = request.POST.get('pk')
		player=Player.objects.get(pk=pk)
		schedule = Schedule.objects.filter(pk=s_pk)
		log_start(request,log_dir+'/'+str(player.pk)+'.log',player.player_name+" deleted schedule : "+str(schdule.pk))
		schedule.delete()
		return HttpResponse("삭제되었습니다!")
	except Exception as e :
		return HttpResponse("delete schedule failed") 

def edit_my_schedule(request) :
	pk = int(request.POST.get('pk'))
	date_start = request.POST.get('date_start')
	date_end = request.POST.get('date_end')
	schedule = Schedule.objects.get(pk=pk)
	schedule.date_start=date_start
	schedule.date_end=date_end
	schedule.save()
	data = {
		'pk' : schedule.pk,
		'title' : schedule.title,
		'date_start' : schedule.date_start,
		'date_end' : schedule.date_end,
		}
	return JsonResponse(data)

def create_match_list(request) :
	matches=Match.objects.all().order_by('-pk')
	serialized_matches= MatchSerializer(matches,many=True)

	pages = request.GET.get('page',0)
	return HttpResponse(json.dumps(serialized_matches.data))

def delete_match_info(request,match_pk) :

	pk=request.session.get('pk')
	player_name = request.GET.get('player_name')

	if pk is None :
			return redirect('/')

	try :
		match=Match.objects.get(pk=match_pk)
		match.delete()
		return redirect('hzm:match')
	except Exception as e :
		print(e)
		return HttpResponse("게시물이 존재하지 않습니다")

	#return render(request, 'hzm/match.html',{'posts' : posts, 'count':count, 'pk':pk, 'player_name':player_name})

def delete_before_match_info(request,match_pk) :
	try :
		pk=request.session.get('pk')
		player_name = request.GET.get('player_name')
		
		if pk is None :
			return redirect('/')

		match=Match.objects.get(pk=match_pk)
		match.delete()
		matches = Match.objects.all().filter(accept=False).order_by('-pk')
		count = matches.count()
		paginator = Paginator(matches, 10)
		pages = request.GET.get('page',1)
		matches = paginator.get_page(pages)
	except PageNotAnInteger :
		matches = paginator.page(1)
	except EmptyPage :
		matches = paginator.page(paginator.num_pages)
		return HttpResponse("end")
	except Exception as e :
		return HttpResponse("게시물이 존재하지 않습니다.")

	return render(request, 'hzm/match_before.html',{'matches' : matches, 'count':count, 'pk':pk, 'player_name':player_name})

def accept_match_info(request,match_pk) :
	pk=request.session.get('pk')
	player_name=request.session.get('player_name')
	if pk is None :
		return redirect('main_page')

	try :
		print(match_pk)
		match=Match.objects.get(pk=match_pk)
		match.accept=True
		match.save()
		matches = Match.objects.all().filter(accept=True).order_by('-pk')

		count = matches.count()
		paginator = Paginator(matches, 10)
		pages = request.GET.get('page',1)
		matches = paginator.get_page(pages)
		print(3)
	except PageNotAnInteger :
		matches = paginator.page(1)
	except EmptyPage :
		matches = paginator.page(paginator.num_pages)
		return HttpResponse("end")

	except Exception as e :
		return HttpResponse("게시물이 존재하지 않습니다.")
	return redirect('hzm:match')
	#return render(request, 'hzm/match.html',{'posts' : posts, 'count':count, 'pk':pk, 'player_name':player_name})

def check_post_passwd(request) :
	passwd=request.POST.get('post_passwd')
	pk = request.POST.get('pk')
	print(passwd)
	match=Match.objects.get(pk=pk)
	
	if passwd == match.passwd :
		data={'team':'blue'}
		return JsonResponse(data)
	elif passwd == club_passwd :
		data={'team':'red'}
		return JsonResponse(data)
	elif passwd == master_passwd :
		data={'team':'all'}
		return JsonResponse(data)
	else :
		data={'team':"fail"}
	return JsonResponse(data)

def save_match_info(request) :
	pk=request.POST.get('match_pk')
	match=Match.objects.get(pk=pk)
	player_num=request.POST.get('player_num')
	match_date=request.POST.get('match_date')
	match_time_start=request.POST.get('time_start')
	match_time_end=request.POST.get('time_end')
	red_goga_avg=request.POST.get('red_goga_avg')
	blue_goga_avg=request.POST.get('blue_goga_avg')
	red_club_id=request.POST.get('red_clud_id')
	red_club_name=request.POST.get('red_clud_name')
	blue_club_name=request.POST.get('blue_clud_name')
	post_writer=request.POST.get('post_writer')
	passwd=request.POST.get('passwd')
	red_win=request.POST.get('red_win')
	blue_win=request.POST.get('blue_win')
	
	players_red=[]
	players_red_id=[]
	players_blue=[]
	if player_num >= '1':
		red_p1_name=request.POST.get('red_p1_name')
		blue_p1_name=request.POST.get('blue_p1_name')
		try :
			player=Player.objects.get(player_name=red_p1_name)
			print("player1")
			print(player.player_name)
			players_red.append(player.player_name)
			players_red_id.append(player.pk)
		except Exception as e :
			print("red1 is none")
		players_blue.append(blue_p1_name)

	if player_num >= '2' :
		red_p2_name=request.POST.get('red_p2_name')
		blue_p2_name=request.POST.get('blue_p2_name')

		try :
			player=Player.objects.get(player_name=red_p2_name)
			print("player2")
			print(player.player_name)
			players_red.append(player.player_name)
			players_red_id.append(player.pk)
		except Exception as e :
			print("red2 is none")
		players_blue.append(blue_p2_name)

	if player_num >= '3' :
		red_p3_name=request.POST.get('red_p3_name')
		blue_p3_name=request.POST.get('blue_p3_name')
		try :
			player=Player.objects.get(player_name=red_p3_name)
			print("player3")
			print(player.player_name)
			players_red.append(player.player_name)
			players_red_id.append(player.pk)
		except Exception as e :
			print("red2 is none")
		players_blue.append(blue_p3_name)
	
	if player_num >= '4' :
		red_p4_name=request.POST.get('red_p4_name')
		blue_p4_name=request.POST.get('blue_p4_name')
		try :
			player=Player.objects.get(player_name=red_p4_name)
			print("player4")
			print(player.player_name)
			players_red.append(player.player_name)
			players_red_id.append(player.pk)
		except Exception as e :
			print("red2 is none")
		players_blue.append(blue_p4_name)

	
	match.red_player_name = players_red
	match.red_player_id = players_red_id
	match.blue_player_name = players_blue
	match.match_date=match_date
	match.match_time_start=match_time_start
	match.match_time_end=match_time_end
	match.red_goga_avg=red_goga_avg
	match.blue_goga_avg=blue_goga_avg
	match.player_num=player_num
	match.red_win=red_win
	match.blue_win=blue_win
	match.save()		
	return redirect('/match/')
	#return render(request, 'hzm/match_info.html', {'post':post, 'pk':pk})
	
	
def save_admin_match_info(request) :
	pk = request.session.get('pk')
	red_club_id=request.POST.get('red_club_id')
	red_club_name=request.POST.get('red_club_name')
	blue_club_name=request.POST.get('blue_club_name')
	post_writer=request.POST.get('post_writer')
	passwd=request.POST.get('passwd')
	player_num=request.POST.get('player_num')
	match_date=request.POST.get('match_date')
	#match_time_start=request.POST.get('time_start')
	#match_time_end=request.POST.get('time_end')
	#red_goga_avg=request.POST.get('red_goga_avg')
	#blue_goga_avg=request.POST.get('blue_goga_avg')
	red_win=request.POST.get('red_win')
	blue_win=request.POST.get('blue_win')
	date = request.POST.get('date')
	result=False
	red_goga_avg="00:00:00"
	blue_goga_avg="00:00:00"
	match_time_start="00:00"
	match_time_end="00:01"
	try :
		temp_player=Player.objects.get(pk=pk)
	except Exception as e :
		return HttpResponse("fail")
	
	players_red=[]
	players_red_id=[]
	players_blue=[]
	if player_num >= '1':
		red_p1_name=request.POST.get('red_p1_name')
		blue_p1_name=request.POST.get('blue_p1_name')
		try :
			player=Player.objects.get(player_name=red_p1_name)
			print("player1")
			print(player.player_name)
			players_red.append(player.player_name)
			players_red_id.append(player.pk)
		except Exception as e :
			print("red1 is none")
		players_blue.append(blue_p1_name)

	if player_num >= '2' :
		red_p2_name=request.POST.get('red_p2_name')
		blue_p2_name=request.POST.get('blue_p2_name')

		try :
			player=Player.objects.get(player_name=red_p2_name)
			print("player2")
			print(player.player_name)
			players_red.append(player.player_name)
			players_red_id.append(player.pk)
		except Exception as e :
			print("red2 is none")
		players_blue.append(blue_p2_name)

	if player_num >= '3' :
		red_p3_name=request.POST.get('red_p3_name')
		blue_p3_name=request.POST.get('blue_p3_name')
		try :
			player=Player.objects.get(player_name=red_p3_name)
			print("player3")
			print(player.player_name)
			players_red.append(player.player_name)
			players_red_id.append(player.pk)
		except Exception as e :
			print("red2 is none")
		players_blue.append(blue_p3_name)
	
	if player_num >= '4' :
		red_p4_name=request.POST.get('red_p4_name')
		blue_p4_name=request.POST.get('blue_p4_name')
		try :
			player=Player.objects.get(player_name=red_p4_name)
			print("player4")
			print(player.player_name)
			players_red.append(player.player_name)
			players_red_id.append(player.pk)
		except Exception as e :
			print("red2 is none")
		players_blue.append(blue_p4_name)

	if red_win > blue_win :
		result=True
	else :
		result=False

	
	match=Match(red_club_id=red_club_id,red_club_name=red_club_name, blue_club_name=blue_club_name \
		,post_writer=post_writer,passwd=passwd \
		,red_player_name=players_red,red_player_id=players_red_id, blue_player_name = players_blue \
		,match_date=match_date, match_time_start=match_time_start, match_time_end=match_time_end \
		,red_goga_avg=red_goga_avg, blue_goga_avg=blue_goga_avg ,date=date\
		,player_num=player_num,red_win=red_win, blue_win=blue_win,state="경기종료",result=result, accept=True)


	match.save()
	log_start(request,log_dir+'/'+str(temp_player.pk)+'.log',player.player_name+" admin add fmatch : "+str(match.pk))		
	return HttpResponse("save")

def get_redteam_subplayer(request) :
	player_num=request.GET.get('player_num')
	red_p1_name=request.GET.get('red_p1')
	red_p2_name=request.GET.get('red_p2')
	red_p3_name=request.GET.get('red_p3')
	red_p4_name=request.GET.get('red_p4')
	club_id=request.GET.get('club_id')

	if player_num == '3' :
		redteam_players=Player.objects.filter(club_id=club_id).exclude(Q(player_name=red_p3_name) |Q(player_name=red_p2_name) | Q(player_name=red_p1_name) ).order_by('player_name')
	elif player_num == '4':
		redteam_players=Player.objects.filter(club_id=club_id).exclude(Q(player_name=red_p4_name) | Q(player_name=red_p3_name) |Q(player_name=red_p2_name) | Q(player_name=red_p1_name) ).order_by('player_name')
	else :
		redteam_players=Player.objects.filter(club_id=club_id).exclude(Q(player_name=red_p2_name) | Q(player_name=red_p1_name) ).order_by('player_name')

	serialized_players = PlayerSerializer(redteam_players,many=True)
	return HttpResponse(json.dumps(serialized_players.data))

def get_redteam_player(request) :
	player_num=request.GET.get('player_num')
	red_p1_name=request.GET.get('red_p1')
	red_p2_name=request.GET.get('red_p2')
	red_p3_name=request.GET.get('red_p3')
	red_p4_name=request.GET.get('red_p4')
	club_id=request.GET.get('club_id')

	if player_num == '3' :
		redteam_players=Player.objects.filter(Q(player_name=red_p3_name) |Q(player_name=red_p2_name) | Q(player_name=red_p1_name) ).order_by('player_name')
	elif player_num == '4':
		redteam_players=Player.objects.filter(Q(player_name=red_p4_name) | Q(player_name=red_p3_name) |Q(player_name=red_p2_name) | Q(player_name=red_p1_name) ).order_by('player_name')
	else :
		redteam_players=Player.objects.filter(Q(player_name=red_p2_name) | Q(player_name=red_p1_name) ).order_by('player_name')

	print(redteam_players)

	serialized_players = PlayerSerializer(redteam_players,many=True)
	return HttpResponse(json.dumps(serialized_players.data))

def save_redteam_player(request) :
	player_num=request.GET.get('player_num')
	
	if player_num >= '1' :
		red_p1_name=request.GET.get('red_p1')
	if player_num >= '2' :
		red_p1_name=request.GET.get('red_p2')
	if player_num >= '3' :
		red_p1_name=request.GET.get('red_p3')
	if player_num >= '4' :
		red_p1_name=request.GET.get('red_p4')

	red_p2_name=request.GET.get('red_p2')
	red_p3_name=request.GET.get('red_p3')
	red_p4_name=request.GET.get('red_p4')

	return HttpResponse("ddd")

def save_matchresult(request) :
	win=request.POST.get('win')
	lose=request.POST.get('lose')
	match_pk =request.POST.get('match_pk')
	player_num=request.POST.get('player_num')

	red_p1_name = request.POST.get('red_p1_name')
	red_p2_name = request.POST.get('red_p2_name')
	if player_num >='3' :
		red_p3_name = request.POST.get('red_p3_name')
	if player_num >='4' :
		red_p4_name = request.POST.get('red_p4_name')

	try :
		match=Match.objects.get(pk=match_pk)
		match.red_win=win
		match.blue_win=lose
		if win > lose :
			match.result=True
		else :
			match.result=False
		match.save()
	except Exception as e :
		print(e)
		return redirect('/')

	return redirect('hzm:match')

def add_map_record(request) :
	maps_id=request.POST.get('maps_id')
	map_record=request.POST.get('record')
	record_date=request.POST.get('record_date')
	player_id=request.session.get('pk')
	player=Player.objects.get(pk=player_id)
	club_id=player.club_id

	try :
		map_=Map.objects.get(pk=maps_id)
		record=Record.objects.get(Q(player_id=player.pk) & Q(maps_id=maps_id))
		record.map_name=map_.map_name
		record.record=map_record
		record.date=record_date
		record.club_id=club_id
	except Exception as e :
		Record.objects.filter(Q(player_id=player.pk) & Q(maps_id=maps_id)).delete()
		record=Record(maps_id=maps_id,map_name=map_.map_name,record=map_record,player_id=player.pk,\
			record_date=record_date,club_id=club_id)
		
	record.save()
	log_start(request,log_dir+'/'+str(player.pk)+'.log',player.player_name+" add record : "+str(record.pk))
	records=Record.objects.filter(Q(player_id=player.pk) & Q(club_id=club_id)).order_by('map_name')
	serialized_records = RecordSerializer(records,many=True)

	return HttpResponse(json.dumps(serialized_records.data))

def get_player_before_auth(request) :
	club_id=request.session.get('club_id')
	players=Player.objects.filter(Q(club_id=club_id) & Q(accept=False))
	serialized_players = PlayerSerializer(players,many=True)		
	return HttpResponse(json.dumps(serialized_players.data)) 

def accept_player(request) :
	club_id=request.session.get('club_id')
	club=Club.objects.get(pk=club_id)
	club.member += 1
	player_name=request.GET.get('player_name')
	player=Player.objects.get(player_name=player_name)
	player.accept=True
	player.save()
	club.save()
	
	return HttpResponse(player_name)
	
def reject_player(request) :
	player_name=request.GET.get('player_name')
	player=Player.objects.get(player_name=player_name)
	player.delete()

	return HttpResponse(player_name)

def add_admin_record(request) :
	club_id=request.session.get('club_id')
	player_id=request.POST.get('player_id')
	maps_id=request.POST.get('maps_id')
	map_record=request.POST.get('record')
	record_date=request.POST.get('record_date')

	try :
		player=Player.objects.get(pk=player_id)
		maps=Map.objects.get(pk=maps_id)
	except Exception as e :
		return HttpResponse(e)
	
	try :
		record=Record.objects.get(Q(player_id=player.pk) & Q(maps_id=maps_id))
		record.record=map_record
		record.date=record_date
		record.map_name=maps.map_name
		record.club_id=club_id
	except Exception as e :
		Record.objects.filter(Q(player_id=player.pk) & Q(maps_id=maps_id)).delete()
		record=Record(maps_id=maps_id,map_name=maps.map_name,record=map_record,player_id=player.pk,\
			record_date=record_date,club_id=club_id)

	record.save()
	log_start(request,log_dir+'/'+str(player.pk)+'.log',player.player_name+" admin add record : "+str(record.pk))
	return HttpResponse("good")


def get_records(request) :
	try :
		player_id=request.session.get('pk')
		club_id=request.session.get('club_id')
		records=Record.objects.filter(Q(player_id=player_id) & Q(club_id=club_id)).order_by('map_name')
		serialized_records = RecordSerializer(records,many=True)	
		
			
		return HttpResponse(json.dumps(serialized_records.data))
	except Exception as e:
		return HttpResponse(e)	



def get_record_rank(request) :
	pk=request.session.get('pk')
	club_id=request.session.get('club_id')

	try :
		all_records=Record.objects.filter(club_id=club_id).values('maps_id').annotate(record=Min('record')).order_by('map_name')
		best_records=[]
		maps=[]
		rank=[]
	
		for i in range(all_records.count()) :
			records=[]
			players=[]
			records_=Record.objects.filter(Q(club_id=club_id)&Q(maps_id=all_records[i]['maps_id'])).values('player_id').annotate(record=Min('record'))

			for k in range(records_.count()) :
				records.append(records_[k]['record'])
				players.append(records_[k]['player_id'])
				
			if pk in players :
				obj_records=Series(records)
				maps.append(all_records[i]['maps_id'])
				best_records.append(all_records[i]['record'])
				rank.append(int(obj_records.rank(method='min')[players.index(pk)]))

		data = {
			'best_record[]': best_records,
			'maps_id[]':maps,
			'rank[]':rank,
		}
		return JsonResponse(data)

	except Exception as e :
		return HttpResponse(e)	

def record_win_lose(player_id,club_id) :
	matches=Match.objects.get.filter(Q(red_club_id=club_id) & Q(red_player_id__contains=[player_id]))
	print(matches)
	return True

def save_club_description(request) :
	try :
		club_id=request.session.get('club_id')
		description=request.POST.get('description')
		print(description)
		club=Club.objects.get(pk=club_id)
		club.description=description
		club.save()
		return HttpResponse("save")
	except Exception as e :
		return HttpResponse("fail")

def add_freeboard_comment(request) :
	pk=request.session.get('pk')
	player_name=request.session.get('player_name')
	post_pk=request.POST.get('post_pk')
	comment=request.POST.get('comment')
	date=getTimeY_M_T()
	try :
		freeboard=Freeboard.objects.get(pk=post_pk)
		freeboard.comment_count += 1
		freeboard.save()
		freeboardcomment=Freeboardcomment(player_id=pk,post_id=post_pk,\
			player_name=player_name,date=date,comments=comment)
		freeboardcomment.save()
		log_start(request,log_dir+'/'+str(pk)+'.log',player_name+" freeboard:"+str(post_pk)+" comment: "+str(freeboardcomment.pk))
	except Exception as e :
		print(e)
		return HttpResponse("fail")

	return HttpResponse("good")


def delete_admin_record(request) :
	try :
		club_id=request.session.get('club_id')
		record_pk=request.GET.get('record_pk')
		record=Record.objects.get(pk=record_pk)
		if record.club_id == club_id :
			record.delete()
			return HttpResponse(record_pk)
		else :
			raise Exception("fail")
	except Exception as e :
		print(e)
		return HttpResponse(e)

def edit_admin_record(request) :
	try :
		club_id=request.session.get('club_id')
		record_pk=request.GET.get('record_pk')
		record_time=request.GET.get('record')
		record=Record.objects.get(pk=record_pk)
		if record.club_id == club_id :
			record.record=record_time
			record.save()
		else :
			raise Exception("fail")
		return HttpResponse("record edit")
	except Exception as e :
		return HttpResponse(e)

def getTimeY_M_T() :
	now = datetime.datetime.now()
	nowDate = now.strftime('%Y-%m-%d %H:%M:%S')
	return nowDate

def get_club_member(request) :
	try :
		club_id=request.session.get('club_id')
		players=Player.objects.filter(Q(club_id=club_id) & Q(accept=True)).order_by('player_name')
		serialized_players = PlayerSerializer(players,many=True)
		return HttpResponse(json.dumps(serialized_players.data))
	except Exception as e :
		return HttpResponse(e)