from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('convert', views.convert, name='convert'),
    path('onquit', views.testcall, name='onquit'),
    
]