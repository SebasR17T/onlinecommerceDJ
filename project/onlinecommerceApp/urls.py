from django.urls import path
from .views import register, login_view, DashboardView, ProductCreateView, ProductListView, ProductDetailView, ProductDeleteView , ProductUpdateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # otras rutas
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('product/create/', ProductCreateView.as_view(), name='crear_producto'),
    path('product/', ProductListView.as_view(), name='listar_producto'),
    path('product/detail/<int:pk>', ProductDetailView.as_view(), name="detalle_producto"),
    path('product/delete<int:pk>', ProductDeleteView.as_view(), name="borrar_producto"),
    path('product/update<int:pk>', ProductUpdateView.as_view(), name="actualizar_producto")

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)