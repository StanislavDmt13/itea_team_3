from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse

class SupportView(TemplateView):
    template_name = 'support.html'

    def get_context_data(self, *args, **kwargs):
        return super().get_context_data(**kwargs)

