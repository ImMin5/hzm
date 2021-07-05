from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import datetime
import json

def getTimeY_M_T() :
	now = datetime.datetime.now()
	nowDate = now.strftime('%Y-%m-%d %H:%M:%S')
	return nowDate


class ChatConsumer(WebsocketConsumer) :
    #연결
    def connect(self) :
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        print("---")
        print(self.room_name)
        self.room_group_name = 'chat_%s' % self.room_name

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    #연결 해제
    def disconnect(self, close_code) :
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
    
    #수신
    def receive(self, text_data) :
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        player_name=text_data_json['player_name']
        chat_time = getTimeY_M_T()

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'player_name' : player_name,
                'chat_time' : chat_time,
            }
        )
     # room group 에서 메세지 receive
    def chat_message(self, event):
        message = event['message']
        player_name = event['player_name']
        chat_time = event['chat_time']

        # WebSocket 에게 메세지 전송
        self.send(text_data=json.dumps({
            'message': message,
            'player_name' : player_name,
            'chat_time' : chat_time,
        }))