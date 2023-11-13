from django.shortcuts import render
from django.template import loader
from django.http import HttpRequest

# Create your views here.
def home_view(request):
    return render(request, 'project_apps/home.html')

def features_view(request):
        return render(request, 'project_apps/features.html')

def about_view(request):
        return render(request, 'project_apps/about.html')