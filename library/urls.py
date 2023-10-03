from django.urls import path
from .views import AddBook, QuickAdd, MyLibrary, BookDetails

urlpatterns = [
    path('add/', AddBook.as_view(), name='add_book'),
    path('q_add/', QuickAdd.as_view(), name='quick_add'),
    path('', MyLibrary.as_view(), name='my_library'),
    path('book/<int:pk>/', BookDetails, name='book_detail')
]
