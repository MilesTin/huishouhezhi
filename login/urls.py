from django.urls import include, path
from .views import *

urlpatterns = [
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("orderCount/",order_count,name="orderCount"),#用户所有的订单数
    path("energySaved/",enery_sum,name="energySaved"),#节省的能量总和
    path('energyUnsaved/',enery_unsaved,name="energyUnsaved"),#能量值
    path("daysSum/",days_sum,name="daysSum"),#餐盒使用总数
    path("saveEnergy",save_energy,name="saveEnergy"),#回收能量池中能量
]