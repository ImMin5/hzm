from django.contrib import admin
from django.urls import path, include
from . import views
from . import apis
from django.conf.urls.static import static
from django.conf import settings

app_name ='hzm'

urlpatterns = [
	path('',views.main_page, name='main_page'),
	path('signin/',views.signin_page,name='signin_page'),
	path('signup/',views.signup_page,name='signup_page'),
	path('api/signin',apis.sign_in,name='ajax_signin'),
	path('api/signup',apis.sign_up,name='ajax_signup'),
	path('api/logout',apis.logout,name='ajax_logout'),
	path('api/add_fmatch',apis.add_fmatch,name='ajax_add_fmatch'),
]