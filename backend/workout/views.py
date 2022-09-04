from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from db.models import *
from .forms import WorkoutsForm, AddCommentForm
from django.views.generic import (UpdateView,
                                  DeleteView,
                                  ListView,
                                  CreateView,
                                  )


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
    total_comments = workout.total_comments()
    return render(request, 'workouts/detail_workout.html', {'workout': workout, 'total_comments': total_comments})


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


class AddCommentView(CreateView):
    model = Comment
    form_class = AddCommentForm
    template_name = 'workouts/add_comment.html'


    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.workout_id = self.kwargs['pk']
        return super().form_valid(form)
