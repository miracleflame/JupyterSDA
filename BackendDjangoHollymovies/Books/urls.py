from django.urls import path
from Books.views import HomepageView, BookListView, BookDetailView, \
    AuthorListView, AuthorDetailView, ContactView, CreateBookView, \
    UpdateBookView,  DeleteBookView, CreateAuthorView, \
    UpdateAuthorView, DeleteAuthorView

urlpatterns = [
    path('', HomepageView.as_view(), name='books_homepage'),
    path('books/', BookListView.as_view(), name='books'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('contact/', ContactView.as_view(), name='contact_view'),
    path('book/create/', CreateBookView.as_view(), name='create_book'),
    path('author/create/', CreateAuthorView.as_view(), name='create_author'),
    path('book/update/<int:pk>/', UpdateBookView.as_view(), name='update_book'),
    path('author/update/<int:pk>/', UpdateAuthorView.as_view(), name='update_author'),
    path('book/delete/<int:pk>/', DeleteBookView.as_view(), name='delete_book'),
    path('author/delete/,<int:pk>/', DeleteAuthorView.as_view(), name='delete_author'),
]
