from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
  path(''       , views.index,  name='index'),
  path('tables/', views.tables, name='tables'),
  path('page_per_mng/', views.page_per_mng, name='page_per_mng'),
  path('page_msg_mng/', views.page_msg_mng, name='page_msg_mng'),
  path('page_sta_insp/', views.page_sta_insp, name='page_sta_insp'),
  path('page_map/', views.page_map, name='page_map'),
]
