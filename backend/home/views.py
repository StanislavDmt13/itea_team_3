from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, UpdateView, FormView, ListView

# Create your views here.
def home_view(*args, **kwargs):
    return HttpResponse("<h1>Hello World!</h1>")


class HomepageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

