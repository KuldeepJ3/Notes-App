from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.models import User

from django import forms

from .models import Note

from django.forms.widgets import PasswordInput, TextInput

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
	username = forms.CharField(widget=TextInput())
	password = forms.CharField(widget=PasswordInput())

class CreateNoteForm(forms.ModelForm):
  class Meta:
    model = Note
    fields = ['title', 'content']
