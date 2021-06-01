from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/lab/(?P<poll_id>\w+)/$', consumers.ChatConsumer.as_asgi()),
]
