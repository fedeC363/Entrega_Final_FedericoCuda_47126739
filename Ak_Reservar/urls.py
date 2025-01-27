from django.urls import path
from .views import ReservaDetailView, ReservaListView, ReservaDeleteView, ReservaUpdateView, ReservaCreateView

urlpatterns = [ 
    path('reservar_list/', ReservaListView.as_view(), name='reservar_list'),
    path('<int:pk>/detail_reservar', ReservaDetailView.as_view(), name='reservar_detail'),
    path('create_reservar/', ReservaCreateView.as_view(), name='reservar_create'),
    path('<int:pk>/update_reservar/', ReservaUpdateView.as_view(), name='reservar_update'),
    path('<int:pk>/delete_reservar/', ReservaDeleteView.as_view(), name='reservar_delete'),
]