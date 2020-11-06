from django.shortcuts import render
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

def signin_page(request) :
	return render(request,'hzm/signin_page.html')

def signup_page(request) :
	return render(request,'hzm/signup_page.html')


