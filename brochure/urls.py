from django.urls import path

from . import views # . stands for current directory, we are importing all views from brochure directory

app_name = 'brochure'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    
]
