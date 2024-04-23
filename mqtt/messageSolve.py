from home.models import Worker


should_save = False
allertMsg = [
    # {
    #     'msg': 'testt',
    # }
]


def addAllert(msg):
    allertMsg.append({
        'msg': msg,
    })


def saveMessage(payload):
    from mqtt.models import Message
    if not should_save:
        return
    Message.objects.create(
        user_id=payload["id"] if "id" in payload else 0,
        temperature=payload["temperature"] if "temperature" in payload else 0,
        humidity=payload["humidity"] if "humidity" in payload else 0,
        volume=payload["volume"] if "volume" in payload else 0,
        iswearing=payload["iswearing"] if "iswearing" in payload else False,
        isfall=payload["isfall"] if "isfall" in payload else False,
        onfire=payload["onfire"] if "onfire" in payload else False,
        workStatus=payload["workStatus"] if "workStatus" in payload else 0,
        location=payload["location"] if "location" in payload else 0,
        timestamp=payload["timestamp"] if "timestamp" in payload else "2021-01-01 12:00:00",
        iscall=payload["iscall"] if "iscall" in payload else False,
        voiceCommand=payload["voiceCommand"] if "voiceCommand" in payload else "",
        gesture=payload["gesture"] if "gesture" in payload else 0,
    )


def solveUnsafe(payload):
    # 在这里处理不安全情况
    # 未戴头盔
    if not payload["iswearing"]:
        print("未戴头盔")
        addAllert(f"员工{payload['id']}未戴头盔，位置在{payload['location']}区域")
    # 音量过大
    if payload["volume"] > 80:
        print("音量过大")
        addAllert(f"员工{payload['id']}环境音量过大，位置在{payload['location']}区域")
    # 温度异常
    if payload["temperature"] > 38.0 or payload["temperature"] < 35.0:
        print("温度异常")
        addAllert(f"员工{payload['id']}体温异常，位置在{payload['location']}区域")
    # 摔倒
    if payload["isfall"]:
        print("摔倒")
        addAllert(f"员工{payload['id']}摔倒，位置在{payload['location']}区域")
    # 起火
    if payload["onfire"]:
        print("起火")
        addAllert(f"员工{payload['id']}处发生火灾，位置在{payload['location']}区域")
    pass


def solveEnv(temp, hum, vol, id, location, timestamp):
    # 在这里处理环境信息
    try:
        worker = Worker.objects.get(id=id)
    except Worker.DoesNotExist:
        pass

    pass


def solveWorkStatus(status, worker_id):
    # 在这里处理工作状态
    try:
        worker = Worker.objects.get(id=id)
        worker.status = status
        worker.save()
    except Worker.DoesNotExist:
        pass

    pass


def solveCall():
    # 处理呼叫 想用于ai
    pass


def solveGesture(gesture):
    # 这里处理手势信息
    if gesture == -1:
        return


def solveMessage(payload):
    print("payload:", payload)
    # payload = {
    #     "id": 1,  # 人员id
    #     "temperature": 36.5,  # 温度
    #     "humidity": 50,  # 湿度
    #     "volume": 50,  # 音量
    #     "iswearing": True,  # 是否佩戴
    #     "isfall": False,  # 是否摔倒
    #     "onfire": False,  # 是否起火
    #     "workStatus": 1,  # 工作状态 1:在岗 2:休息 3:请假 4:其他
    #     "location": 1,  # 位置 1:A区 2:B区 3:C区
    #     "timestamp": "2021-01-01 12:00:00",  # 时间戳
    #     "iscall": False,  # 是否呼叫 用于语音传输
    #     "voiceCommand": "请离开该区域",  # 语音指令
    #     "gesture": 1,  # 手势 -1表示没有
    # }

    # 处理不安全情况
    solveUnsafe(payload)

    # 处理基本环境数据
    solveEnv(temp=payload["temperature"],
             hum=payload["humidity"],
             vol=payload["volume"],
             id=payload["id"],
             location=payload["location"],
             timestamp=payload["timestamp"])

    # 处理工作状态
    solveWorkStatus(payload["workStatus"], worker_id=payload["id"])

    # 处理语音指令
    if payload["iscall"]:
        solveCall()

    # 处理手势信息
    solveGesture(payload["gesture"])

    # 保存数据
    saveMessage(payload)
