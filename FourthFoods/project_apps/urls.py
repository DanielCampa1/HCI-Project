from django.urls import path
from . import views

app_name = 'project_apps'

urlpatterns = [
    path('', views.home_view, name="home"),
    path('features/', views.features_view, name="features"),
    path('about/', views.about_view, name="about"),
    path('dashboard/', views.dashboard_view, name="dashboard"),
    path('create/', views.create_view, name="create"),
    path('history/', views.history_view, name="history"),
    path('signup/', views.SignUp_View, name='signup')

]