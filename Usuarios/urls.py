from django.urls import path
from . import views 

urlpatterns = [    
    path('login/', views.login, name= "login"),
    path('cadastro/', views.cadastro, name= "cadastro"),
    path('validar_cadastro/', views.validar_cadastro, name = "validar_cadastro"),
    path('validar_login/', views.validar_login, name = "validar_login"),
    path('cadastrar_filtros/', views.cadastrar_filtros, name="cadastrar_filtros"),
    path('home/', views.home, name="home"),
    path('sair/', views.sair, name= "sair")
]