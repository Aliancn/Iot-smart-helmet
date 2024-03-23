from django.shortcuts import render, redirect
from admin_datta.forms import RegistrationForm, LoginForm, UserPasswordChangeForm, UserPasswordResetForm, UserSetPasswordForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from django.views.generic import CreateView
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required

from .models import *

def index(request):

  context = {
    'segment'  : 'index',
    #'products' : Product.objects.all()
  }
  return render(request, "pages/index.html", context)

def tables(request):
  context = {
    'segment': 'tables'
  }
  return render(request, "pages/dynamic-tables.html", context)

def page_per_mng(request):
  context = {
    'segment': 'page_per_mng'
  }
  return render(request, "iot-pages/page-per-mng.html", context)

def page_msg_mng(request):
  context = {
    'segment': 'page_msg_mng'
  }
  return render(request, "iot-pages/page-msg-mng.html", context)

def page_sta_insp(request):
  context = {
    'segment': 'page_sta_insp'
  }
  return render(request, "iot-pages/page-sta-insp.html", context)

def page_map(request):
  context = {
    'segment': 'page_map'
  }
  return render(request, "iot-pages/page-map.html", context)
