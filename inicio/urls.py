from django.urls import path
from inicio import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('mesas/', views.ListarMesas.as_view(), name='listar_mesas'),
    path('mesas/crear/', views.CrearMesa.as_view(), name='crear_mesa'),
    # path('mesas/<int:pk>/', views.VerMesa.as_view(), name='ver_mesa'),
    path('mesas/<int:pk>/editar/', views.EditarMesa.as_view(), name='editar_mesa'),
    path('mesas/<int:pk>/eliminar/', views.EliminarMesa.as_view(), name='eliminar_mesa')
]
