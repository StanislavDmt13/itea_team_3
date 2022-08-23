from django.shortcuts import render
from django.views.generic import TemplateView


class ProgramsView(TemplateView):
    template_name = 'programs.html'
