from django.shortcuts import render, redirect
from db.models import Workouts
from .forms import WorkoutsForm
from django.views.generic import DetailView, UpdateView, DeleteView


def my_workout(request):
    workout = Workouts.objects.filter(user=request.user).order_by('-date_create')
    return render(request, 'workouts/workouts.html', {'workout': workout})


def detail_workout(request, pk):
    workout = Workouts.objects.get(pk=pk)
    return render(request, 'workouts/detail_workout.html', {'workout': workout})


class WorkoutUpdatelView(UpdateView):
    model = Workouts
    template_name = 'workouts/create_workout.html'
    form_class = WorkoutsForm


class WorkoutDeletelView(DeleteView):
    model = Workouts
    success_url = '/workout/'
    template_name = 'workouts/delete_workout.html'


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
