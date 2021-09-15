from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('elevar',views.elevar, name="elevar")
]