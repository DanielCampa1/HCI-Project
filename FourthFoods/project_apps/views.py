from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpRequest
from django.views.generic import CreateView, DetailView
from django.contrib.auth.decorators import login_required  #For function based view protection
from django.contrib.auth.mixins import LoginRequiredMixin  #For class based view protection
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.urls import reverse_lazy

# Create your views here.
def home_view(request):
    return render(request, 'project_apps/home.html')

def features_view(request):
    return render(request, 'project_apps/features.html')

def about_view(request):
    return render(request, 'project_apps/about.html')

#Logged In views
@login_required
def dashboard_view(request):
    return render(request, 'project_apps/dashboard.html')

@login_required
def create_view(request):
    return render(request, 'project_apps/create.html')

@login_required
def history_view(request):
    return render(request, 'project_apps/history.html')


def SignUp_View(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'project_apps/home.html')
    else:
        form = SignUpForm()
    return render(request, 'project_apps/signup.html', {'form': form})