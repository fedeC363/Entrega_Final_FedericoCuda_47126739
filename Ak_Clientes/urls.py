from django.urls import path
from .views import index, about

urlpatterns = [ 
    path('menu/', index, name='menu'),
    path('about/', about, name='about'),
]