from django.urls import path
from . import views

urlpatterns = [
    path('', views.modules_dashboard, name='modules-dashboard'),
    path('install/<int:pk>/', views.install_module, name='install-module'),
    path('uninstall/<int:pk>/', views.uninstall_module, name='uninstall-module'),
    path('upgrade/<int:pk>/', views.upgrade_module, name='upgrade-module'),
]