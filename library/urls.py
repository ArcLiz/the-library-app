# library urls

from django.urls import path
from .views import AddBook, QuickAdd, MyLibrary, EditBook, book_details

urlpatterns = [
    path('add/', AddBook.as_view(), name='add_book'),
    path('q_add/', QuickAdd.as_view(), name='quick_add'),
    path('', MyLibrary.as_view(), name='my_library'),
    path('book/<int:pk>/', book_details, name='book_detail'),
    path('edit/<int:pk>/', EditBook.as_view(), name='edit_book'),
]
