from django.urls import path
from . import views

urlpatterns = [
    path("", views.nordeste, name="nordeste"),
    path("ceara", views.ceara, name="ceara"),
    path("bahia", views.bahia, name="bahia"),
    path("pernambuco", views.pernambuco, name="pernambuco"),
    
]