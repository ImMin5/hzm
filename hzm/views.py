from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from hzm.models import *
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
import json
# Create your views here.


def main_page(request) :
	pk=request.session.get('pk')
	player_id=request.session.get('player_id') 
	return render(request,'hzm/main_page.html',{'pk':pk ,'player_id':player_id})

def schedule(request) :
	pk=request.session.get('pk')

	print('schedule page')
	print(pk)
	if pk is not None :
		return render(request, 'hzm/schedule.html')
	else :
		return redirect('/')


def signin_page(request) :
	return render(request,'hzm/signin_page.html')

def signup_page(request) :
	return render(request,'hzm/signup_page.html')


