from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    #path('convert', views.imgtopdfConvert, name='convert'),
    path('onquit', views.onquit, name='onquit'),
    path('home', views.home, name='home'),
    path('getstarted', views.getStarted, name='getstarted'),
    path('imgtopdfconvert', views.imgtopdfConvert, name='imgtopdfconvert'),
    path('imgtopdfupload', views.imgtopdfUpload, name='imgtopdfupload'),

    
    
]