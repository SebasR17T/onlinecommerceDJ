from django.urls import path
from .views import register

urlpatterns = [
    # otras rutas
    path('register/', register, name='register'),
]
