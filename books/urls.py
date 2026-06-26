from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('<int:pk>/', views.book_detail, name='book_detail'),
    path('add/', views.book_add, name='book_add'),
    path('<int:pk>/update/', views.book_update, name='book_update'),
    path('<int:pk>/delete/', views.book_delete, name='book_delete'),
]