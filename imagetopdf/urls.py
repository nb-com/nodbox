from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('onquit', views.onquit, name='onquit'),
    path('home', views.home, name='home'),
    path('getstarted', views.getStarted, name='getstarted'),
    path('convert', views.getStarted, name='getstarted'),
    path('imgtopdfconvert', views.imgtopdfConvert, name='imgtopdfconvert'),
    path('imgtopdfupload', views.imgtopdfUpload, name='imgtopdfupload'),
    path('download', views.download, name='download'),

    
    
]