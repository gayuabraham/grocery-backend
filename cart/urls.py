from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_cart),
    path('add/', views.add_to_cart),
    path('remove/<int:id>/', views.remove_cart),
]