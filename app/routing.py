from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/sensor-data/$', consumers.SensorDataConsumer.as_asgi()),
    re_path(r'ws/digital-data/$', consumers.DigitalDataConsumer.as_asgi()),
]
