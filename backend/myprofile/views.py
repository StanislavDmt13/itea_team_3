from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, UpdateView, FormView
from db.models import User
from .forms import UserForm, UserAvatar


class HomepageView(TemplateView,LoginRequiredMixin):
    template_name = 'profile.html'


class ProfileEditView(UpdateView, FormView, LoginRequiredMixin):
    model = User
    form_class = UserForm
    avatar_form_class = UserAvatar
    template_name = 'edit.html'
    success_url = '/myprofile'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        kwargs['active_client'] = True
        if 'form' not in kwargs:
            kwargs['form'] = self.form_class(instance=self.get_object())
        if 'avatar_form' not in kwargs:
            kwargs['avatar_form'] = self.avatar_form_class(instance=self.get_object())

        return super(ProfileEditView, self).get_context_data(**kwargs)

@login_required
def change_avatar(request):
    if request.method == 'POST':
        data = UserAvatar(request.POST, request.FILES, instance=request.user)
        if data.is_valid():
            data.save()
            return HttpResponseRedirect(reverse('myprofile-homepage'))
