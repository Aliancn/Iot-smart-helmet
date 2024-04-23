import json
from django.http import JsonResponse
from django.shortcuts import render
from mqtt.mqtt import client as mqtt_client
# Create your views here.
from mqtt.messageSolve import allertMsg


def publish_message(request):
    # 发送mqtt消息
    request_data = json.loads(request.body)
    topic = request_data['topic']
    msg = json.dumps({"msg": request_data['msg']})
    rc, mid = mqtt_client.publish(topic=topic, payload=msg, qos=1)
    return JsonResponse({'code': rc})


def allert(request):
    msg = []
    # 响应报警
    if len(allertMsg) > 0:
        for alt in allertMsg:
            msg.append(alt['msg'])
            # 删除该条报警
        allertMsg.clear()
    return JsonResponse({'msg': msg})
