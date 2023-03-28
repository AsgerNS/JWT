from rest_framework import generics, permissions
from .models import Book, OrderBook
from .serializers import BookSerializer, OrderBookSerializer


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrderedBookList(generics.ListCreateAPIView):
    queryset = OrderBook.objects.all()
    serializer_class = OrderBookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class OrderedBookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderBook.objects.all()
    serializer_class = OrderBookSerializer
    permission_classes = [permissions.IsAuthenticated]
