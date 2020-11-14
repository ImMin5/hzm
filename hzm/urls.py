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
	path('match/',views.match,name='match'),
	path('match/info/<int:post_pk>/',views.match_info,name='match_info'),
	path('match_before/',views.match_before,name='match_before'),
	path('match_before/info/<int:post_pk>/',views.match_before_info,name='match_before_info'),
	path('mypage/',views.mypage, name='mypage'),
	path('api/signin',apis.sign_in,name='ajax_signin'),
	path('api/signup',apis.sign_up,name='ajax_signup'),
	path('api/logout',apis.logout,name='ajax_logout'),
	path('api/add_fmatch',apis.add_fmatch,name='ajax_add_fmatch'),
	path('api/add_schedule',apis.add_schedule,name='ajax_add_schedule'),
	path('api/get_my_schedules',apis.get_my_schedules,name='ajax_get_my_schedules'),
	path('api/get_all_schedules',apis.get_all_schedules,name='ajax_get_all_schedules'),
	path('api/create_my_schedule_table',apis.create_my_schedule_table,name='ajax_create_my_schedule_table'),
	path('api/id_check',apis.id_check, name='ajax_id_check'),
	path('api/id_check_btn',apis.id_check_btn, name='ajax_id_check_btn'),
	path('api/delete_my_schedule',apis.delete_my_schedule, name='ajax_delete_my_schedule'),
	path('api/edit_my_schedule',apis.edit_my_schedule, name='ajax_edit_my_schedule'),
	path('api/crate_post_list',apis.create_post_list, name='ajax_create_post_list'),
	path('api/edit_mypage_info',apis.edit_mypage_info, name='ajax_edit_mypage_info'),
	path('api/delete_before_match_info/<int:post_pk>/',apis.delete_before_match_info, name='delete_before_match_info'),
	path('api/delete_match_info/<int:post_pk>/',apis.delete_match_info, name='delete_match_info'),
	path('api/accept_match_info/<int:post_pk>/',apis.accept_match_info, name='accept_match_info'),
	path('api/check_post_passwd',apis.check_post_passwd,name='ajax_check_post_passwd'),
	path('api/save_match_info',apis.save_match_info,name='ajax_save_match_info'),
	path('api/get_redteam_player',apis.get_redteam_player,name='ajax_get_redteam_player'),
	path('api/get_redteam_subplayer',apis.get_redteam_subplayer,name='ajax_get_redteam_subplayer'),
	path('api/save_redteam_player',apis.save_redteam_player,name='ajax_save_redteam_player'),
	path('error',views.error_page,name='error_page'),
	path('api/save_matchresult',apis.save_matchresult,name='ajax_save_matchresult'),
	path('personal_record',views.personal_record,name='personal_record'),
]