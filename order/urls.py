from django.urls import include, path
from .views import *

urlpatterns = [
    path("new_order/",new_order,name="new_order"),
    path("verif_order/",verif_order,name="verif_order"),
    path("order_complete",order_complete,name="order_complete"),

]