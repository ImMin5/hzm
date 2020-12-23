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

def getTimeY_M_T() :
	now = datetime.datetime.now()
	nowDate = now.strftime('%Y-%m-%d %H:%M:%S')
	return nowDate

def add_freeboard_writing(request) :
	pk=request.session.get('pk')
	club_id=request.session.get('club_id')
	title=request.POST.get('title')
	description=request.POST.get('description')
	date=getTimeY_M_T()
	try :
		player=Player.objects.get(pk=pk)
		post=Freeboard(player_id=player.pk,club_id=club_id,post_writer=player.player_name,\
			title=title,date=date,description=description)
		post.save()
		log_start(request,request,log_dir+'/'+str(player.pk)+'.log',"freeboard writing "+str(post.pk))
		return HttpResponse("good")
	except Exception as e :
		print(e)
		return HttpResponse(e)


def delete_freeboardcomment(request) :
    try :
        pk=request.session.get('pk')
        player=Player.objects.get(pk=pk)
        comment_pk=request.POST.get('comment_pk')
        comment=Freeboardcomment.objects.get(pk=comment_pk)
        log_start(request,log_dir+'/'+str(player.pk)+'.log',player.player_name+" delete comment("+str(comment.pk)+") "+comment.comments)
        print("delete")
        comment.delete()
        return HttpResponse(comment_pk)
    except Exception as e :
        print(e)
        return HttpResponse("fail")

def edit_freeboard_writing(request) :
    pk=request.session.get('pk')
    club_id=request.session.get('club_id')
    title=request.POST.get('title')
    description=request.POST.get('description')
    freeboard_pk=request.POST.get('freeboard_pk')
    try :
        player=Player.objects.get(pk=pk)
        post=Freeboard.objects.get(pk=freeboard_pk)
        post.title=title
        post.description=description
        post.save()
        log_start(request,log_dir+'/'+str(player.pk)+'.log','freeboard edit '+str(post.pk))
        return HttpResponse("save")
    except Exception as e :
        print(e)
        return HttpResponse(e)

def delete_freeboard_writing(request) :
    freeboard_pk = request.POST.get('freeboard_pk')
    try :
        post=Freeboard.objects.get(pk=freeboard_pk)
        post.delete()
        return HttpResponse("delete")
    except Exception as e :
        return HttpResponse("fail")
