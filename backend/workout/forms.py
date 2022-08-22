from db.models import *
from django.forms import ModelForm, TextInput, Textarea, NumberInput


class WorkoutsForm(ModelForm):
    class Meta:
        model = Workouts
        exclude = ['user']
        fields = ['name_workout', 'exercise_name', 'number_of_approaches', 'amount_of_exercise',
                  'distance', 'workout_time', 'photo_workout', 'description']

        widgets = {
            'name_workout': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Workout name'
            }),
            'exercise_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name of the exercise'
            }),
            'number_of_approaches': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Number of approaches'
            }),
            'amount_of_exercise': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Number of exercises'
            }),
            'distance': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Distance traveled'
            }),
            'workout_time': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Workout time'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Description of the workout'
            }),
        }
