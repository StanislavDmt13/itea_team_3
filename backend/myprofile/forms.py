from django import forms
from django.forms import ModelForm
from db.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name',
                  'last_name', 'phone', 'email',)

        labels = {'username': '',
                  'first_name': '',
                  'last_name': '',
                  'phone': '',
                  'email': '',
                  }

        widgets = {'username': forms.TextInput(attrs={'class': 'form-control-3 ', 'placeholder': 'Username'}),
                   'first_name': forms.TextInput(attrs={'class': 'form-control-3', 'placeholder': 'First_name'}),
                    'last_name': forms.TextInput(attrs={'class': 'form-control-3', 'placeholder': 'Last_name'}),
                    'phone': forms.TextInput(attrs={'class': 'form-control-3', 'placeholder': 'Phone'}),
                    'email': forms.EmailInput(attrs={'class': 'form-control-3', 'placeholder': 'Email'}),
                 }


class UserAvatar(ModelForm):
    class Meta:
        model = User
        fields = ('avatar',)