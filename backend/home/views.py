from django.views.generic import TemplateView
from db.models import Workouts, Category


class HomepageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        kwargs['workout'] = \
            Workouts.objects.filter(user=self.request.user, is_privet=False).order_by('-date_create')[:5]
        kwargs['categories'] = Category.objects.all()
        if self.request.user.is_authenticated:
            self.template_name = 'profile.html'
        return super().get_context_data(**kwargs)

