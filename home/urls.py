from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index,  name='index'),
    path('tables/', views.tables, name='tables'),
    path('page_per_mng/', views.page_per_mng, name='page_per_mng'),
    path('page_msg_mng/', views.page_msg_mng, name='page_msg_mng'),
    path('page_sta_insp/', views.page_sta_insp, name='page_sta_insp'),
    path('page_map/', views.page_map, name='page_map'),
    path('page_per_stu/', views.person_status, name='page_per_stu'),
    path('send_msg/', views.send_msg, name='send_msg'),
    path('profile/<int:worker_id>/edit/', views.edit_profile, name='edit_profile'),
    path('profile/<int:worker_id>/save/', views.save_profile, name='save_profile'),
    path('profile/<int:worker_id>/delete/', views.delete_profile, name='delete_profile'),
    path('profile/add/', views.add_profile, name='add_profile'),
    path('profile/add_save/', views.add_save_profile, name='add_save_profile'),
    path('create-workers/', views.create_workers, name='create_workers'),  
    path('test/', views.test , name='test'),
]
