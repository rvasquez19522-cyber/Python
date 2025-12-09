# chat_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para el admin
    path('', include('chat_app.urls')),  # Incluir las URLs de chat_app
]
