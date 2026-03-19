from django.urls import path
from .views import create_order, user_orders

urlpatterns = [

    path("create/", create_order),
    path("my-orders/", user_orders),
]