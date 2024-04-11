from django.shortcuts import render, redirect
from admin_datta.forms import RegistrationForm, LoginForm, UserPasswordChangeForm, UserPasswordResetForm, UserSetPasswordForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from django.views.generic import CreateView
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required

from .models import *


def index(request):

    context = {
        'segment': 'index',
        # 'products' : Product.objects.all()
    }
    return render(request, "pages/index.html", context)


def tables(request):
    context = {
        'segment': 'tables'
    }
    return render(request, "pages/dynamic-tables.html", context)


def page_per_mng(request):
  workers = Worker.objects.all()

  context = {
    'segment': 'page_per_mng',
    'workers': workers
  }
  return render(request, "iot-pages/page-per-mng.html", context)

def page_msg_mng(request):
    workers = Worker.objects.all()
    context = {
        'segment': 'page_msg_mng',
        'workers': workers
    }
    return render(request, "iot-pages/page-msg-mng.html", context)


def page_sta_insp(request):

    workers = Worker.objects.all().values()
    msgs = Msg.objects.all().values()

    context = {
        'segment': 'page_sta_insp',
        'workers': [
            {'id': 12321, 'name': 'John Doe', 'status': '在岗', 'location': 'A区'},
            {'id': 12453, 'name': 'Jane Doe', 'status': '休息', 'location': '\\'},
            {'id': 12754, 'name': 'John Smith', 'status': '请假', 'location': '\\'},
        ],
        'msgs': [
            {'id': 12321, 'describe': 'dsadsada',
                'timestamp': '2021-01-01 12:00:00'},
            {'id': 12321, 'describe': 'dsadsada',
                'timestamp': '2021-01-01 12:00:00'},
            {'id': 12321, 'describe': 'dsadsada',
                'timestamp': '2021-01-01 12:00:00'},
            {'id': 12321, 'describe': 'dsadsada',
                'timestamp': '2021-01-01 12:00:00'},
            {'id': 12321, 'describe': 'dsadsada',
                'timestamp': '2021-01-01 12:00:00'},
            {'id': 12321, 'describe': 'dsadsada',
                'timestamp': '2021-01-01 12:00:00'},
            {'id': 12321, 'describe': 'dsadsada',
                'timestamp': '2021-01-01 12:00:00'},
            {'id': 12321, 'describe': 'dsadsada',
                'timestamp': '2021-01-01 12:00:00'},
            {'id': 12321, 'describe': 'dsadsada',
                'timestamp': '2021-01-01 12:00:00'},
        ],
        'donut': [
            {'label': '在岗', 'value': 60},
            {'label': '休息', 'value': 20},
            {'label': '请假', 'value': 10},
            {'label': '其他', 'value': 10},
        ],
        'mydata_line': [
            {'y': '2006', 'a': 100, 'b': 90},
            {'y': '2007', 'a': 75, 'b': 65},
            {'y': '2008', 'a': 50, 'b': 40},
            {'y': '2009', 'a': 75, 'b': 65},
            {'y': '2010', 'a': 50, 'b': 40},
            {'y': '2011', 'a': 75, 'b': 65},
            {'y': '2012', 'a': 100, 'b': 90}
        ],
    }
    return render(request, "iot-pages/page-sta-insp.html", context)


def page_map(request):
    context = {
        'segment': 'page_map'
    }
    return render(request, "iot-pages/page-map.html", context)


def person_status(request):
    class Status():
        ACTIVE = '在岗'
        INACTIVE = '休息'
        PENDING = '请假'
        OTHER = '其他'
    context = {
        'segment': 'person_status',
        'workers': [
            {'id': 12321, 'name': 'John Doe', 'status': Status.ACTIVE,
                'location': 'A区', 'safe': True, 'temperature': '36.5', 'helmet': True},
            {'id': 12453, 'name': 'Jane Doe', 'status': Status.INACTIVE,
                'location': '\\', 'safe': True, 'temperature': '36.5', 'helmet': True},
            {'id': 12754, 'name': 'John Smith', 'status': Status.PENDING,
                'location': '\\', 'safe': True, 'temperature': '36.5', 'helmet': True},

        ],
    }
    return render(request, "iot-pages/page-per-statu.html", context)

def send_msg(request):
    workerId = request.POST.getlist('workerId')
    msgId = request.POST.getlist('msgId')

    for id in workerId:
        print(id)
    
    for id in msgId:
        print(id)

    workers = Worker.objects.all()
    context = {
        'workers': workers
    }
    # testmessage 
    # 警告类
    # id 内容
    # 01 有危险，请离开该区域
    # 02 请马上佩戴头盔
    # 03 小心操作
    # 消息类
    # id 内容
    # 11 不要偷懒
    # 12 下班啦
    # 13 不要闲聊

    # 暂时未做检验人员/消息为空的警告逻辑，以及提交成功的按钮
    return render(request, "iot-pages/page-msg-mng.html", context)
