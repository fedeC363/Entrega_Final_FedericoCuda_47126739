from django.urls import path
from .views import register, editarPerfil
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('registrar/', register, name='registrar'),
    path('editar_perfil/', editarPerfil, name='editar_Perfil'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
