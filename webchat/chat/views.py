# chat/views.py

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('<h1>Chat</h1><p><a href="/chat/test/">Entrar en sala "test"</a></p>')

def room(request, room_name):
    return HttpResponse(f'<h1>Sala: {room_name}</h1><p>Aquí iría el chat.</p>')
