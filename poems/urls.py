from django.urls import path
from . import views

urlpatterns = [
  path('hello/', views.HelloView.as_view(), name='HelloView'),
  path('poem/', views.PoemList.as_view(), name='poems'),
  path('poem/<int:pk>/', views.PoemDetail.as_view(), name='poem')
]