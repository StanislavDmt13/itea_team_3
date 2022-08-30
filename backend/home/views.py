from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse

class HomepageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            self.template_name = 'profile.html'
        return super().get_context_data(**kwargs)

