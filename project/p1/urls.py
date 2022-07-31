from django.urls import path
from . import views

urlpatterns = [
    path('p1index/', views.p1index),
]