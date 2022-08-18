from django.urls import path
from . import views

urlpatterns = [
    path('p2/', views.p2),
    path('index/', views.inedx)
]