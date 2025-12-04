from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Room(models.Model):
    """Sala de xat"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_private = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def get_messages(self, limit=50):
        """Obté els últims missatges de la sala"""
        return self.messages.all().order_by('-timestamp')[:limit][::-1]


class Message(models.Model):
    """Missatge del xat"""
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_edited = models.BooleanField(default=False)
    edited_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['timestamp']
    
    def __str__(self):
        return f"{self.user.username}: {self.content[:50]}"
    
    def edit(self, new_content):
        """Edita el missatge"""
        self.content = new_content
        self.is_edited = True
        self.edited_at = timezone.now()
        self.save()


class UserProfile(models.Model):
    """Perfil d'usuari ampliat"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar_color = models.CharField(max_length=7, default='#007bff')
    bio = models.TextField(max_length=500, blank=True)
    is_online = models.BooleanField(default=False)
    last_seen = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Perfil de {self.user.username}"
    
    def set_online(self):
        self.is_online = True
        self.last_seen = timezone.now()
        self.save()
    
    def set_offline(self):
        self.is_online = False
        self.last_seen = timezone.now()
        self.save()