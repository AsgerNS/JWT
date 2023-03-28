from django.urls import path
from .views import BookList, BookDetail
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('books/', BookList.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book_detail'),
    # path('ordered_books/', OrderedBookList.as_view(), name='ordered_book_list'),
    # path('ordered_books/<int:pk>/', OrderedBookDetail.as_view(), name='ordered_book_detail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]