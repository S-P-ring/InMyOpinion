from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('index1/', views.index1),
    path('manage_appeal/', views.manage_appeal),
    path('null_appeal/', views.null_appeal),
    path('publicate/', views.publicate),
    path('edit/', views.edit),
    path('end_edit', views.end_edit),
]