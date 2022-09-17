from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('email/', include('enviar_email.urls')),
    path('auth/', include('Usuarios.urls'))
]
