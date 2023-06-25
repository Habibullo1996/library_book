from django.urls import path
from .views import BookApiView, BookCreateAPIView, BookDetailAPIView, \
    BookDeleteAPIView, BookUpdateAPIView

urlpatterns = [
    path('books/', BookApiView.as_view(), name='books_list'),
    path('book/create/', BookCreateAPIView.as_view(), name='book_create'),
    path('book/<int:pk>/detail/', BookDetailAPIView.as_view(), name='book_detail'),
    path('book/<int:pk>/delete/', BookDeleteAPIView.as_view(), name='book_delete'),
    path('book/<int:pk>/update/', BookUpdateAPIView.as_view(), name='book_update'),

]
