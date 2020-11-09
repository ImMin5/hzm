from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from hzm.models import *
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
import json
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.


def main_page(request) :
	pk=request.session.get('pk')
	player_name=request.session.get('player_id') 
	return render(request,'hzm/main_page.html',{'pk':pk ,'player_id':player_name})

def mypage(request) :
	pk=request.session.get('pk')
	player_name=request.session.get('player_id')

	player=Player.objects.get(pk=pk)
	return render(request,'hzm/mypage.html',{'pk':pk ,'player_id':player_name,'player':player})

def schedule(request) :
	pk=request.session.get('pk')
	player_name=request.session.get('player_id')
	print('schedule page')
	print(pk)
	if pk is not None :
		return render(request, 'hzm/schedule.html',{'pk':pk, 'player_id':player_name})
	else :
		return redirect('/')


def signin_page(request) :
	return render(request,'hzm/signin_page.html')

def signup_page(request) :
	return render(request,'hzm/signup_page.html')

def match(request) :
	count = Post_list.objects.all().count()
	posts = Post_list.objects.all().order_by('-pk')
	paginator = Paginator(posts, 2)
	pages = request.GET.get('page',1)

	pk=request.session.get('pk')
	player_name=request.session.get('player_id') 

	try :
		posts = paginator.get_page(pages)
	except PageNotAnInteger :
		posts = paginator.page(1)
	except EmptyPage :
		posts = paginator.page(paginator.num_pages)
		return HttpResponse("end")

	return render(request, 'hzm/match.html',{'posts' : posts, 'post_count':count, 'pk':pk, 'player_id':player_name})

def match_result(request,post_pk) :
	pk=request.session.get('pk')
	player_id=request.session.get('player_id') 
	post = Post_list.objects.get(pk=post_pk)
	return render(request, 'hzm/match_result.html', {'post':post,'time_start':post.match_time_start,\
		'time_end':post.match_time_end ,'pk':pk, 'player_id':player_name})


