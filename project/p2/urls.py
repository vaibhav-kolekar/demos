from django.urls import path
from . import views

urlpatterns = [
    path('p2index/', views.p2index),
]