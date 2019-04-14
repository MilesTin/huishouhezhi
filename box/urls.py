from . import views
from django.urls import include, path
from .models import heZhi

urlpatterns = [
    path('getall/',views.getall,name="getall"),
    path('getbox<int:boxId>/',views.getbox,name="getBox"),
]