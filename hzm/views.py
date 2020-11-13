from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from django.urls import reverse
from hzm.models import *
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
import json
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
#from datetime import datetime
# Create your views here.


def main_page(request) :
	pk=request.session.get('pk')
	player_name=request.session.get('player_name') 
	return render(request,'hzm/main_page.html',{'pk':pk ,'player_name':player_name})

def mypage(request) :
	pk=request.session.get('pk')
	player_name=request.session.get('player_name')

	if pk is None :
		request.session.clear()
		return redirect('/')
		
	try : 
		player=Player.objects.get(pk=pk)
	except Exception as e :
		return redirect('/')
	return render(request,'hzm/mypage.html',{'pk':pk ,'player_name':player_name,'player':player})

def schedule(request) :
	pk=request.session.get('pk')
	player_name=request.session.get('player_name')
	print('schedule page')
	print(pk)
	if pk is not None :
		return render(request, 'hzm/schedule.html', {'pk':pk, 'player_name':player_name})
	else :
		return redirect('/')


def signin_page(request) :
	return render(request,'hzm/signin_page.html')

def signup_page(request) :
	return render(request,'hzm/signup_page.html')

def match(request) :

	posts = Post_list.objects.all().filter(state=True).order_by('-pk')
	count = posts.count();
	paginator = Paginator(posts, 10)
	pages = request.GET.get('page',1)

	pk=request.session.get('pk')
	player_name=request.session.get('player_name') 

	try :
		posts = paginator.get_page(pages)
	except PageNotAnInteger :
		posts = paginator.page(1)
	except EmptyPage :
		posts = paginator.page(paginator.num_pages)
		return HttpResponse("end")

	return render(request, 'hzm/match.html',{'posts' : posts, 'post_count':count, 'pk':pk, 'player_name':player_name})

def match_info(request,post_pk) :
	pk=post_pk
	player_name=request.session.get('player_name') 

	if pk is None :
		return redirect("/")
	elif player_name is None :
		return redirect("/")

	post = Post_list.objects.get(pk=pk)
	return render(request, 'hzm/match_info.html', {'post':post, 'pk':pk})

def match_before_info(request,post_pk) :
	try :
		pk=request.session.get('pk')
		player_name=request.session.get('player_name') 

		if pk is None :
			return redirect("/")
		elif player_name is None :
			return redirect("/")

		post = Post_list.objects.get(pk=post_pk)
		if post.state == True :
			raise Exception('error')
		return render(request, 'hzm/match_before_info.html', {'post':post, 'pk':pk, 'player_name':player_name})
	except Exception as e :
		return HttpResponseRedirect(reverse('hzm:error_page'))

def match_before(request) :

	pk=request.session.get('pk')
	player_name=request.session.get('player_name') 

	if pk is None :
		return redirect("/")
	elif player_name is None :
		return redirect("/")

	posts = Post_list.objects.all().filter(state=False).order_by('-pk')
	count = posts.count()
	paginator = Paginator(posts, 10)
	pages = request.GET.get('page',1)

	try :
		posts = paginator.get_page(pages)
	except PageNotAnInteger :
		posts = paginator.page(1)
	except EmptyPage :
		posts = paginator.page(paginator.num_pages)
		return HttpResponse("end")

	return render(request, 'hzm/match_before.html',{'posts' : posts, 'count':count, 'pk':pk, 'player_name':player_name})

def delete_result(request) :
	return render(request,'hzm/test.html')

def error_page(request) :
	return render(request, 'hzm/error.html')
