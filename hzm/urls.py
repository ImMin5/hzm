from django.contrib import admin
from django.urls import path, include
from . import views
from . import apis
from django.conf.urls.static import static
from django.conf import settings

app_name ='hzm'

urlpatterns = [
	path('',views.main_page, name='main_page'),
	path('schedule/', views.schedule, name='schedule'),
	path('signin/',views.signin_page,name='signin_page'),
	path('signup/',views.signup_page,name='signup_page'),
	path('api/signin',apis.sign_in,name='ajax_signin'),
	path('api/signup',apis.sign_up,name='ajax_signup'),
	path('api/logout',apis.logout,name='ajax_logout'),
	path('api/add_fmatch',apis.add_fmatch,name='ajax_add_fmatch'),
	path('api/add_schedule',apis.add_schedule,name='ajax_add_schedule'),
	path('api/get_my_schedules',apis.get_my_schedules,name='ajax_get_my_schedules'),
	path('api/get_all_schedules',apis.get_all_schedules,name='ajax_get_all_schedules'),
	path('api/create_my_schedule_table',apis.create_my_schedule_table,name='ajax_create_my_schedule_table'),
	path('api/id_check',apis.id_check, name='ajax_id_check'),
	path('api/delete_my_schedule',apis.delete_my_schedule, name='ajax_delete_my_schedule'),
	path('api/edit_my_schedule',apis.edit_my_schedule, name='ajax_edit_my_schedule'),

]