from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

from PythonBots.consumer import ChatConsumer#, TaskConsumer

application = ProtocolTypeRouter({ 
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    #url(r"chat/", ChatConsumer, name='chat')
                    url(r"posts/$", ChatConsumer, name='chat'),
                    url(r'^posts/messages/$', ChatConsumer),

                ]
                )
            )
        )

})

