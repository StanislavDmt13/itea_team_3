from django.views.generic import TemplateView

class HomepageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            self.template_name = 'profile.html'
        return super().get_context_data(**kwargs)

