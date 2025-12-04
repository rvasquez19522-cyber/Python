# chat/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="chat_index"),            # /chat/
    path("<str:room_name>/", views.room, name="chat_room"),  # /chat/<room>/
]
