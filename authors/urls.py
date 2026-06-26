from django.urls import path
from . import views

urlpatterns = [
    path('', views.author_list, name='author_list'),
    path('<int:pk>/', views.author_detail, name='author_detail'),
    path('add/', views.author_add, name='author_add'),
    path('<int:pk>/update/', views.author_update, name='author_update'),
    path('<int:pk>/delete/', views.author_delete, name='author_delete'),
]