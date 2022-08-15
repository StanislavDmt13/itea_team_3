from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import NewUserForm


def user_login(request):
    if request.method == "POST":
        email = request.POST['Email']
        password = request.POST['Password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, "Welcome back! How's it going out there?")
            return HttpResponseRedirect(reverse('myprofile-homepage'))
        else:
            messages.error(request, "Wrong username or password. Don't take it too hard.")
            return HttpResponseRedirect(reverse('login_user'))
    else:
        return render(request, 'registration/login.html')


def user_registration(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('myprofile-homepage'))

    else:
        form = NewUserForm()
    return render(request, "registration/registration.html", {"register_form": form})
