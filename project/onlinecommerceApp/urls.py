from django.urls import path
from .views import register, login_view, DashboardView

urlpatterns = [
    # otras rutas
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('dashboard/', DashboardView.as_view(), name='dashboard')

]
