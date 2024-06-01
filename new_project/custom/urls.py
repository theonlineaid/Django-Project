from django.urls import path
from . import views

urlpatterns = [
    path('custom/', views.custom, name='custom'),
]