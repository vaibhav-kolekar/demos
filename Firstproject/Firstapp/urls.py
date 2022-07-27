from django.urls import path
from . import views

urlpatterns = [
    path('funone/', views.funone),
]