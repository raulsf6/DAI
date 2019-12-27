# miaplicacion/urls.py

from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('groups/', views.groups, name='groups'),
  path('groups/new/', views.object_new, name='groups_new'),
  path('musicians/', views.musicians, name='musicians'),
  path('musicians/new/', views.object_new, name='musicians_new'),
  path('albums/', views.albums, name='albums'),
  path('albums/new/', views.object_new, name='albums_new'),
  path('groups/<int:pk>/', views.object_detail, name='group_detail'),
  path('albums/<int:pk>/', views.object_detail, name='album_detail'),
  path('musicians/<int:pk>/', views.object_detail, name='musician_detail'),
  path('albums/<int:pk>/edit/', views.album_edit, name='album_edit'),
  path('groups/<int:pk>/edit/', views.group_edit, name='group_edit'),
  path('musicians/<int:pk>/edit/', views.musician_edit, name='musician_edit'),
  path('musicians/<int:pk>/delete/', views.object_delete, name='musician_delete'),
  path('groups/<int:pk>/delete/', views.object_delete, name='group_delete'),
  path('albums/<int:pk>/delete/', views.object_delete, name='album_delete'),
]

