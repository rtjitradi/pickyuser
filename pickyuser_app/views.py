from django.shortcuts import render, HttpResponseRedirect, reverse

from custom_user.settings import AUTH_USER_MODEL

from pickyuser_app.forms import LoginForm, SignUpForm

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def index_view(request):
    settings_authusermod = AUTH_USER_MODEL
    return render(request, 'index.html', {'page_title': 'CustomUser: Homepage', 'settings_authusermod': settings_authusermod})


def signup_view(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            signup_data = signup_form.cleaned_data
            signup_newuser = SignUpForm.objects.create_user(
                username=signup_data.get('username'),
                password=signup_data.get('password'),
                display_name=signup_data.get('display_name'),
                age=signup_data.get('age'),
                homepage=signup_data.get('homepage')
            )
            if signup_newuser:
                login(request, signup_newuser)
                return HttpResponseRedirect(reverse('home'))

    signup_form = SignUpForm()
    return render(request, {'page_title': 'CustomUser: SignUp Form', 'signup_form': signup_form})


def login_view(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            login_data = login_form.cleaned_data
            user = authenticate(
                request, username=login_data.get('username'),
                password=login_data.get('password')
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))

    login_form = LoginForm()
    return render(request, 'login.html', {'page_title': 'CustomUser: LoginForm', 'login_form': login_form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
