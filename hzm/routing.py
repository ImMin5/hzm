from django.urls import path, include
from . import consumers

websocket_urlpatterns = {
    path('ws/chat/club/<int:room_name>/',consumers.ChatConsumer.as_asgi(),name="clubchat")
}