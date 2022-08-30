from django import forms
from db.models import TrainProgram
from django.forms import ModelForm


class TrainForm(ModelForm):
    class Meta:
        model = TrainProgram
        fields = ('name', 'author', 'tasks')