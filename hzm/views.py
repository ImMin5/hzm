from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from django.urls import reverse
from hzm.models import *
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
import json
import datetime
import time
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.db.models import Q
#from datetime import datetime
# Create your views here.

def record_win_lose(player_id,club_id) :
	matches=Match.objects.filter(Q(club_red_id=club_id) & Q(red_player_id__contains=[player_id]))
	player=Player.objects.get(pk=player_id)
	player.win=0
	player.lose=0
	for match in matches :
		if match.red_win > match.blue_win :
			player.win += 1
		else :
			player.lose += 1
	player.save()
	return ;



def main_page(request) :
	pk=request.session.get('pk')
	club_id=request.session.get('club_id')
	#records=Record.objects.all().order_by('maps_id')
	#maps=Map.objects.all().order_by('pk')

	
	
	if pk is not None :
		player=Player.objects.get(pk=pk)
		club=Club.objects.get(pk=player.club_id)
		return render(request,'hzm/main_page.html',{'pk':pk,'player':player,'club':club})
	else :
		return render(request,'hzm/main_page.html')

def mypage(request) :
	pk=request.session.get('pk')

	if pk is None :
		request.session.clear()
		return redirect('/')
		
	try : 
		player=Player.objects.get(pk=pk)
		club=Club.objects.get(pk=player.club_id)
	except Exception as e :
		return redirect('/')
	return render(request,'hzm/mypage.html',{'pk':pk ,'player':player,'club':club})

def schedule(request) :
	pk=request.session.get('pk')
	player_name=request.session.get('player_name')
	try :
		if pk is not None :
			player=Player.objects.get(pk=pk)
			club=Club.objects.get(pk=player.club_id)
			return render(request, 'hzm/schedule.html', {'pk':pk, 'player':player, 'club':club})
		else :
			return redirect('/')
	except Exception as e :
		return redirect('/')



def signin_page(request) :
	return render(request,'hzm/signin_page.html')

def signup(request) :
	pk = request.session.get('pk')

	if pk is not None :
		return redirect('hzm:main_page')
		
	clubs=Club.objects.all()
	return render(request,'hzm/signup.html',{'clubs':clubs})

def match(request) :
	pk=request.session.get('pk')
	club_id = request.session.get('club_id')
	matches = Match.objects.all().filter(Q(accept=True)).order_by('-match_date')
	count = matches.count()
	paginator = Paginator(matches, 10)
	pages = request.GET.get('page',1)
	
	clubs=Club.objects.all().order_by('club_name')

	now = time.strftime('%Y-%m-%d %I:%M',time.localtime())
	for match in matches :
		match_date_start = match.match_date+' '+match.match_time_start
		match_date_end = match.match_date+' '+match.match_time_end

		if match_date_start > now :
			match.state="경기준비"
		elif match_date_end < now :
			match.state="경기종료"
		else :
			match.state="진행중"

		match.save()

	try :
		matches = paginator.get_page(pages)
	except PageNotAnInteger :
		matches = paginator.page(1)
	except EmptyPage :
		matches = paginator.page(paginator.num_pages)
		return HttpResponse("end")

	if pk :
		player=Player.objects.get(pk=pk)
		club=Club.objects.get(pk=player.club_id)
		return render(request, 'hzm/match.html',{'matches' : matches, 'match_count':count ,'pk':pk ,'clubs':clubs,'club':club})
	else :
		return render(request, 'hzm/match.html',{'matches' : matches, 'match_count':count})


def match_info(request,match_pk) :
	match_pk=match_pk
	pk=request.session.get('pk')
	player_name=request.session.get('player_name') 
	club_id=request.session.get('club_id')
	
	try :
		club=Club.objects.get(pk=club_id)
		match = Match.objects.get(pk=match_pk)
	except Exception as e :
		return render(request, 'hzm/error.html')
	
	if match.accept == False :
		return render(request, 'hzm/error.html')
	return render(request, 'hzm/match_info.html', {'match':match, 'pk':pk, 'club':club})

def match_before_info(request,match_pk) :
	
	try :
		match=Match.objects.get(pk=match_pk)
		if match.accept == True :
			raise("잘못된접근")
		pk=request.session.get('pk')
		player_name=request.session.get('player_name') 
		club_id=request.session.get('club_id')
		club=Club.objects.get(pk=club_id)
		try :			
			if match.club_red_id != club_id :
				return render(request,'hzm:main_page.html')
		except Exception as e:
			return render('hzm:error')


		if pk is None :
			return redirect("/")
		elif player_name is None :
			return redirect("/")

		match = Match.objects.get(pk=match_pk)

		if match.accept == True :
			raise('error')

		return render(request, 'hzm/match_before_info.html', {'match':match, 'pk':pk, 'player_name':player_name,'club':club})
	except Exception as e :
		print(e)
		return HttpResponseRedirect(reverse('hzm:error_page'))

def match_before(request) :

	pk=request.session.get('pk')
	player_name=request.session.get('player_name') 
	club_id=request.session.get('club_id')

	if pk is None :
		return redirect('/')

	try :
		club=Club.objects.get(pk=club_id)
		player=Player.objects.get(pk=pk)
	except Exception as e :
		return redirect('/')

	matches = Match.objects.all().filter(Q(accept=False) & Q(club_red_id=club_id)).order_by('-pk')
	count = matches.count()
	paginator = Paginator(matches, 2)
	pages = request.GET.get('page',1)

	try :
		matches = paginator.get_page(pages)
	except PageNotAnInteger :
		matches = paginator.page(1)
	except EmptyPage :
		matches = paginator.page(paginator.num_pages)
		return HttpResponse("end")

	return render(request, 'hzm/match_before.html',{'matches' : matches, 'count':count, 'pk':pk, 'player_name':player_name,'club':club})

def delete_result(request) :
	return render(request,'hzm/test.html')

def error_page(request) :
	return render(request, 'hzm/error.html')

def personal_record(request) :
	player_name=request.session.get('player_name')
	pk=request.session.get('pk')
	club_id=request.session.get('club_id')
	maps=Map.objects.all().order_by('map_name')	
	records=Record.objects.filter(player_id=pk).order_by('map_name')

	try :
		player=Player.objects.get(pk=pk)
		club=Club.objects.get(pk=club_id)
		record_win_lose(pk,club_id)
	except Exception as e :
		print(e)
		return redirect("/")

	if pk is None :
		return redirect("/")
		

	return render(request, 'hzm/personal_record.html',{'records':records,'maps':maps,'player':player ,'pk':pk,'club':club})

def club(request,club_pk) :
	pk=request.session.get('pk')
	club_id=request.session.get('club_id')

	if pk is None :
		return redirect('/')
	try :
		player=Player.objects.get(pk=pk)
		club=Club.objects.get(pk=club_id)
		print(club)
		return render(request, 'hzm/club.html',{'pk':pk,'player':player,'club':club})
	except Exception as e :
		print(e)
		return redirect('/')

def match_form(request) :
	pk = request.session.get('pk')
	club_id = request.session.get('club_id')
	clubs=Club.objects.all()

	if pk is not None :
		club=Club.objects.get(pk=club_id)
		return render(request,'hzm/match_form.html',{'pk':pk,'club':club,'clubs':clubs})	
	return render(request,'hzm/match_form.html',{'clubs':clubs})


def match_filter(request) :

	pk=request.session.get('pk')
	club_id = request.session.get('club_id')
	condition=request.GET.get('filter')
	print(condition)
	if condition != "전체" :
		posts = Post_list.objects.all().filter(Q(accept=True) & Q(club_id=condition)).order_by('-pk')
	else :
		posts = Post_list.objects.all().filter(Q(accept=True)).order_by('-pk')

	count = posts.count();
	paginator = Paginator(posts, 10)
	pages = request.GET.get('page',1)

	
	clubs=Club.objects.all().order_by('-pk')

	now = time.strftime('%Y-%m-%d %I:%M',time.localtime())
	for post in posts :
		match_date_start = post.match_date+' '+post.match_time_start
		match_date_end = post.match_date+' '+post.match_time_end
		print(now)
		print(match_date_end)
		if match_date_start > now :
			post.state="경기준비"
		elif match_date_end < now :
			post.state="경기종료"
		else :
			post.state="진행중"
		print(post.state)
		post.save()

	try :
		posts = paginator.get_page(pages)
	except PageNotAnInteger :
		posts = paginator.page(1)
	except EmptyPage :
		posts = paginator.page(paginator.num_pages)
		return HttpResponse("end")

	if pk :
		player=Player.objects.get(pk=pk)
		club=Club.objects.get(pk=player.club_id)
		return render(request, 'hzm/match.html',{'posts' : posts, 'post_count':count ,'pk':pk ,'clubs':clubs,'club':club})
	else :
		return render(request, 'hzm/match.html',{'posts' : posts, 'post_count':count})


def club_admin(request,club_pk) :
	try :
		pk=request.session.get('pk')
		player_name=request.session.get('player_name')
		club=Club.objects.get(pk=club_pk)
		if club.host != player_name :
			raise Exception('잘못된 접근입니다')
		players=Player.objects.filter(club_id=club.pk)
		maps=Map.objects.all().order_by('map_name')
		records=Record.objects.all().order_by('player_id')
		return render(request,'hzm/admin.html',{'pk':pk,'players':players,'maps':maps,'records':records, 'club':club})
	except Exception as e :
		return redirect('/')

def matchred(request) :
	matchreds = Matchred.objects.all().order_by('player_name')
	matchred = Matchred.objects.get(pk=5)


	return render(request, 'hzm/test.html',{'matchreds':matchreds,'matchred':matchred })