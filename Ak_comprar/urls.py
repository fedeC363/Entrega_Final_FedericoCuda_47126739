from django.urls import path
from .views import ComprarDetailView, ComprarListView, ComprarDeleteView, ComprarUpdateView, ComprarCreateView

urlpatterns = [ 
    path('comprar_list/', ComprarListView.as_view(), name='comprar_list'),
    path('<int:pk>/', ComprarDetailView.as_view(), name='comprar_detail'),
    path('create/', ComprarCreateView.as_view(), name='comprar_create'),
    path('<int:pk>/update/', ComprarUpdateView.as_view(), name='comprar_update'),
    path('<int:pk>/delete/', ComprarDeleteView.as_view(), name='comprar_delete'),
]