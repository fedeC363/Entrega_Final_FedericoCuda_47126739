from django.urls import path
from .views import index, fede

urlpatterns = [
    
    path('', index, name='index'),
    path('fede/', fede, name='fede'),
]