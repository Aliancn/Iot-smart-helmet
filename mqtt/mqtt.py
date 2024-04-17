import json
import paho.mqtt.client as mqtt
from django.conf import settings

from mqtt.messageSolve import solveMessage

topic = [("django/helmet/test1", 1), ("django/helmet/test2", 1)]


def on_connect(mqtt_client, userdata, flags, rc):
    if rc == 0:
        print('Connected successfully')
        mqtt_client.subscribe(topic)
    else:
        print('Bad connection. Code:', rc)

def func1(payload):
    print('Function 1')

def func2(payload):
    print('Function 2')


def on_message(mqtt_client, userdata, msg):
    # print(f'Received message on topic: {msg.topic} with payload: {msg.payload}')
    msg.payload = msg.payload.decode('utf-8')
    payload_json = json.loads(msg.payload)
    print(
        f'Received message on topic: {msg.topic} with payload: {payload_json}, {type(payload_json)}')
    # 多重选择语句
    # 按照topic的不同，执行不同的函数
    switch = {
        "topic1": func1,
        "topic2": func2,
        "test/1": solveMessage  # 测试时用于处理数据
    }
    switch[msg.topic](payload_json)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)
client.connect(
    host=settings.MQTT_SERVER,
    port=settings.MQTT_PORT,
    keepalive=settings.MQTT_KEEPALIVE
)
