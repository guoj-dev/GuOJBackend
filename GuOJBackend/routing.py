from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import BaseMiddleware,AuthMiddleware
from django.urls import path,include

application = ProtocolTypeRouter({
    'websocket': AuthMiddleware(
        URLRouter(
            [

            ]
        )
    )
})