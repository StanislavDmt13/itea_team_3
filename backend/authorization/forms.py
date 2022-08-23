from django import forms
from django.contrib.auth.forms import UserCreationForm
from db.models import User


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name',
                  'phone', 'email', 'password1',
                  'password2')

    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].label = ''
            if field == 'password1' or field == 'password2':
                self.fields[field].widget.attrs['placeholder'] = 'Password'
            else:
                self.fields[field].widget.attrs['placeholder'] = field.title

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        if commit:
            user.save()
            return user
