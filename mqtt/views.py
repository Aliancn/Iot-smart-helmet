import json
from django.http import JsonResponse
from django.shortcuts import render
from mqtt.mqtt import client as mqtt_client
# Create your views here.

def publish_message(request):
    request_data = json.loads(request.body)
    topic = request_data['topic']
    msg = json.dumps({"msg":request_data['msg']})
    rc, mid = mqtt_client.publish(topic=topic,payload=msg,qos=1)
    return JsonResponse({'code': rc})