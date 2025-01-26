from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from Ak_Usuarios.views import register

urlpatterns = [ 
    path('', LoginView.as_view(template_name='Ak_LogIn/login.html'), name='login'),
    path('', LogoutView.as_view(), name='logout'),
    path('registrar/', register, name='registrar')
]