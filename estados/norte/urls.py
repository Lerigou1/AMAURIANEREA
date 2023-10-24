from django.urls import path
from . import views

urlpatterns = [
    path("", views.norte, name = "norte"),
    path("tocantins", views.tocantins, name = "tocantins"),
    path("acre", views.acre, name = "acre"),

    
]