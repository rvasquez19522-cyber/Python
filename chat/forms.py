from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Room, Message, UserProfile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'description', 'is_private']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de la sala'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripció'}),
            'is_private': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Escriu el teu missatge...',
                'id': 'message-input'
            })
        }
        labels = {
            'content': ''
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar_color', 'bio']
        widgets = {
            'avatar_color': forms.TextInput(attrs={'type': 'color', 'class': 'form-control form-control-color'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }