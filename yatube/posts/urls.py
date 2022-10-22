from poplib import POP3_SSL_PORT
from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name = 'posts_start'),
    path('group/<slug:slug>/', views.group_posts, name = 'group_list'),
] 