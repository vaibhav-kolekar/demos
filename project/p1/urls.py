from django.urls import path
from . import views

urlpatterns = [
    path('p1/', views.p1),
    path('index/', views.index),
]