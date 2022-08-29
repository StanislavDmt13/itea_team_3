from django.views.generic import TemplateView

class MainView(TemplateView):
    template_name = 'support.html'

    def get_context_data(self, *args, **kwargs):
        return super().get_context_data(**kwargs)

