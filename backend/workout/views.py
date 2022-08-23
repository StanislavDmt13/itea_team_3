from django.shortcuts import render, redirect
from db.models import Workouts
from .forms import WorkoutsForm


def my_workout(request):
    workout = Workouts.objects.filter(user=request.user)
    return render(request, 'workouts/workouts.html', {'workout': workout})


def create_workout(request):
    if request.method == 'POST':
        form = WorkoutsForm(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('workout')

    form = WorkoutsForm()
    img_obj = form.instance

    data = {
        'form': form,
        'img_obj': img_obj
    }
    return render(request, 'workouts/create_workout.html', data)
