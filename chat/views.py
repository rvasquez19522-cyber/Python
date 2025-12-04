from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Count, Q
from .models import Room, Message, UserProfile
from .forms import RegisterForm, RoomForm, MessageForm, UserProfileForm

def register(request):
    """Registre d'usuaris"""
    if request.user.is_authenticated:
        return redirect('chat:index')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Crear perfil d'usuari
            UserProfile.objects.create(user=user)
            login(request, user)
            messages.success(request, f'Benvingut/da {user.username}!')
            return redirect('chat:index')
    else:
        form = RegisterForm()
    
    return render(request, 'chat/register.html', {'form': form})


def user_login(request):
    """Login d'usuaris"""
    if request.user.is_authenticated:
        return redirect('chat:index')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if hasattr(user, 'profile'):
                user.profile.set_online()
            messages.success(request, f'Benvingut/da de nou, {user.username}!')
            return redirect('chat:index')
        else:
            messages.error(request, 'Usuari o contrasenya incorrectes')
    
    return render(request, 'chat/login.html')


@login_required
def user_logout(request):
    """Logout d'usuaris"""
    if hasattr(request.user, 'profile'):
        request.user.profile.set_offline()
    logout(request)
    messages.info(request, 'Has tancat la sessió correctament')
    return redirect('chat:login')


@login_required
def index(request):
    """Pàgina principal amb llista de sales"""
    rooms = Room.objects.annotate(
        message_count=Count('messages')
    ).order_by('-created_at')
    
    context = {
        'rooms': rooms,
    }
    return render(request, 'chat/index.html', context)


@login_required
def room(request, room_name):
    """Vista de la sala de xat"""
    chat_room = get_object_or_404(Room, name=room_name)
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.room = chat_room
            message.save()
            messages.success(request, 'Missatge enviat!')
            return redirect('chat:room', room_name=room_name)
    else:
        form = MessageForm()
    
    # Obtenir missatges
    room_messages = chat_room.get_messages(limit=100)
    
    # Obtenir usuaris online a la sala (simplificat)
    online_users = UserProfile.objects.filter(is_online=True)
    
    context = {
        'room': chat_room,
        'messages': room_messages,
        'form': form,
        'online_users': online_users,
    }
    return render(request, 'chat/room.html', context)


@login_required
def create_room(request):
    """Crear una nova sala"""
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.created_by = request.user
            room.save()
            messages.success(request, f'Sala "{room.name}" creada correctament!')
            return redirect('chat:room', room_name=room.name)
    else:
        form = RoomForm()
    
    return render(request, 'chat/create_room.html', {'form': form})


@login_required
def profile(request):
    """Perfil d'usuari"""
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualitzat correctament!')
            return redirect('chat:profile')
    else:
        form = UserProfileForm(instance=profile)
    
    # Estadístiques de l'usuari
    total_messages = Message.objects.filter(user=request.user).count()
    
    context = {
        'form': form,
        'profile': profile,
        'total_messages': total_messages,
    }
    return render(request, 'chat/profile.html', context)


@login_required
@require_POST
def delete_message(request, message_id):
    """Eliminar un missatge"""
    message = get_object_or_404(Message, id=message_id, user=request.user)
    room_name = message.room.name
    message.delete()
    messages.success(request, 'Missatge eliminat')
    return redirect('chat:room', room_name=room_name)


@login_required
@require_POST
def edit_message(request, message_id):
    """Editar un missatge"""
    message = get_object_or_404(Message, id=message_id, user=request.user)
    new_content = request.POST.get('content', '')
    
    if new_content:
        message.edit(new_content)
        messages.success(request, 'Missatge editat')
    
    return redirect('chat:room', room_name=message.room.name)


@login_required
def get_messages(request, room_name):
    """API per obtenir missatges nous (AJAX)"""
    room = get_object_or_404(Room, name=room_name)
    last_id = request.GET.get('last_id', 0)
    
    new_messages = Message.objects.filter(
        room=room,
        id__gt=last_id
    ).select_related('user', 'user__profile')
    
    messages_data = [{
        'id': msg.id,
        'user': msg.user.username,
        'content': msg.content,
        'timestamp': msg.timestamp.strftime('%H:%M'),
        'avatar_color': msg.user.profile.avatar_color if hasattr(msg.user, 'profile') else '#007bff',
        'is_own': msg.user == request.user,
    } for msg in new_messages]
    
    return JsonResponse({'messages': messages_data})