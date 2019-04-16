from . import views
from django.urls import include, path
from .models import heZhi

urlpatterns = [
    path('getall/',views.getall,name="getall"),
    path('getbox<int:boxId>/',views.getbox,name="getBox"),
    path('get7dayavg/',views.getSevenDayAvg,name="get7dayavg"),
    path("getboxcount/",views.getLunchBoxCount,name="getboxcount"),
]