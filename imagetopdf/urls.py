from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('convert', views.convert, name='convert'),
    path('onquit', views.onquit, name='onquit'),
    path('home', views.home, name='home'),
    
]