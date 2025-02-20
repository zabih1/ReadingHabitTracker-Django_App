from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('current/', views.current_books, name='current_books'),
    path('tech/', views.tech_books, name='tech_books'),
    path('novels/', views.novel_books, name='novel_books'),
    path('book/<int:book_id>/update/', views.update_book_status, name='update_book_status'),
    path('book/<int:book_id>/delete/', views.delete_book, name='delete_book'),
    path('tech/add/', views.add_tech_book, name='add_tech_book'),
    path('novels/add/', views.add_novel_book, name='add_novel_book'),
]