from django.shortcuts import render
from django.http import JsonResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'index.html')

def sensor_data_api(request):
    value = request.GET.get('value', 0)
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "sensor_data",
        {
            "type": "send_sensor_data",
            "data": value,
        }
    )
    return JsonResponse({"status": "ok"})



def digital_data_api(request):
    value = request.GET.get('value', 0)

    print(f"Digital keldi: {value}")

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "digital_data",
        {
            "type": "send_digital_data",
            "data": value
        }
    )

    return JsonResponse({"status": "ok"})

