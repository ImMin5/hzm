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
from rest_framework.response import Response
from django.core.files.storage import default_storage #파일 저장 경로
from django.conf import settings
from django.db.models import Q
from django.utils.dateparse import parse_date



def sign_in(request) :
	player_id = request.POST.get('player_id')
	player_passwd = request.POST.get('player_passwd')
	
	if request.method == 'POST' :
		print('POST')
		print(player_id)
		print(player_passwd)

		player = Player.objects.get(Q(player_id=player_id) & Q(player_passwd=player_passwd))
		data = {}
		print(player.pk)
		if player is not None:
			print('login')
			#data['pk'] = player_pk
			request.session['pk'] = player.pk
			request.session['player_id'] = player.player_id
			return redirect('/')
		else :
			print('NONE')
			return HttpResponse('Login failed. Try again2.')
	else :
		return HttpResponse('Login failed. Try again1.')


def sign_up(request) :
	player_id = request.POST.get('player_id')
	player_passwd = request.POST.get('player_passwd')
	club_name = request.POST.get('player_club')
	
	if request.method == 'POST' :
		print('POST')
		print(player_id)
		print(player_passwd)
		if Player.objects.get(player_id=player_id) :
			return HttpResponse('중복된 닉네임')
		player = Player(player_id=player_id, player_passwd=player_passwd, club_name=club_name)
		player.save()

		player = Player.objects.get(player_id=player_id)
		request.session['pk'] = player.pk
		request.session['player_id'] = player.player_id

		if player is not None:
			print('create id')
			return redirect('/')
		else:
			print('NONE')
			return HttpResponse('아이디 생성실패1')
	else :
		return HttpResponse('아이디생성실패2')


def logout(request) :
	request.session.clear()
	return redirect('/')


def add_fmatch(request) :
	post_writer = request.POST.get('post_writer');
	club_name = request.POST.get('club_name');
	match_date = request.POST.get('match_date');
	match_time_start = request.POST.get('match_time_start');
	match_time_end = request.POST.get('match_time_end');
	player_num = request.POST.get('player_num');
	passwd = request.POST.get('passwd');
	players = request.POST.getlist('player[]')

	print(match_date)
	post_list = Post_list(post_writer=post_writer, club_name=club_name, match_date=match_date, match_time_start=match_time_start, match_time_end=match_time_end, post_passwd=passwd)
	post_list.save();

	return HttpResponse("good")


