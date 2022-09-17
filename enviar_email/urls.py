from django.urls import path
from . import views 

urlpatterns = [    
    path('teste/', views.cria_template, name="teste")
]
