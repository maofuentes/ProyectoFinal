from django.contrib import admin
from django.urls import path
from productos import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", views.home, name="home"),
    path("listar_usuarios/", views.listar_usuarios, name="listar_usuarios"),
    path("crear_usuarios/", views.crear_usuarios, name="crear_usuarios"),
    path("login_usuarios/", views.login_usuarios, name="login_usuarios"),
    path("datos_usuarios/", views.datos_usuarios, name="datos_usuarios"),
    path("logout_usuarios/", views.logout_usuarios, name="logout_usuarios"),
    path("panel_admin/", views.panel_admin, name="panel_admin"),
]
