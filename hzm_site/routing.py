from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
import hzm.routing

application = ProtocolTypeRouter({
    "http" :get_asgi_application(),
    'websocket' : AuthMiddlewareStack(
        URLRouter(
            hzm.routing.websocket_urlpatterns
        )
    )
})