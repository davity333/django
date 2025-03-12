from django.urls import path 
from .consumers import MyConsumer
from .sendSocket import MyConsumer
websocket_urlpatterns = [
    path('ws/consumers/', MyConsumer.as_asgi()),
    path('ws/consumers/add', MyConsumer.as_asgi()),
]