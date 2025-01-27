from django.urls import path
from .views import ComentarioDetailView, ComentarioListView, ComentarioDeleteView, ComentarioUpdateView, ComentarioCreateView

urlpatterns = [ 
    path('comentar_list/', ComentarioListView.as_view(), name='comentar_list'),
    path('<int:pk>/detail_comment', ComentarioDetailView.as_view(), name='comentar_detail'),
    path('create_comment/', ComentarioCreateView.as_view(), name='comentar_create'),
    path('<int:pk>/update_comment/', ComentarioUpdateView.as_view(), name='comentar_update'),
    path('<int:pk>/delete_comment/', ComentarioDeleteView.as_view(), name='comentar_delete'),
]