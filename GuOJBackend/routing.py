from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import BaseMiddleware,AuthMiddleware

application = ProtocolTypeRouter({
    'websocket': AuthMiddleware(
        URLRouter(
            [

            ]
        )
    )
})