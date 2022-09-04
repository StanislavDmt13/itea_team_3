from django.shortcuts import render, redirect
from db.models import Workouts
from .forms import WorkoutsForm
from django.views.generic import UpdateView, DeleteView, ListView


class MyWorkout(ListView):
    paginate_by = 4
    model = Workouts
    context_object_name = 'workout'
    template_name = 'workouts/workouts.html'

    def get_context_data(self, **kwargs):
        kwargs['workout'] = Workouts.objects.filter(user=self.request.user).order_by('-date_create')
        return super().get_context_data(**kwargs)


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
            print(form)
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
