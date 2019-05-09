from django.urls import include, path
from .views import *

urlpatterns = [
    path("new_order/",new_order,name="new_order"),
    path("order_complete",order_complete,name="order_complete"),
    path("order_sum",order_sum,name="order_sum"),#所有的订单数，餐盒使用次数
    path("days_sum",days_sum,name="days_sum"),#所有餐盒使用的天数
]