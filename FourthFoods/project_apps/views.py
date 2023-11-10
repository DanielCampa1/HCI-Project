from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def home_view(request):
    return render(request, 'project_apps/home.html')