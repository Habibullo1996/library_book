from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import BookSerializer
from .models import Book


class BookApiView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data_result = {
            'status': f"Returned {len(books)} books",
            'books': serializer_data
        }
        return Response(data_result)


class BookCreateAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)


        if serializer.is_valid():
            serializer.save()

            context = {
                'status': f" books are saved  to the database",
                'books': data
            }

            return Response(context)
        else:
            return Response({
                'status': False,
                'message': "Serializer is not valid"
            }, status=status.HTTP_400_BAD_REQUEST)


class BookDetailAPIView(APIView):
    def get(self, pk, request):
        try:
            book = Book.objects.get(id=pk)
            serializer_data = BookSerializer(book).data
            context = {
                'status': "Successfull",
                'book': serializer_data
            }
            return Response(context, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({
                'status': "Does not exists",
                'message': "book is not found"
            }, status=status.HTTP_404_NOT_FOUND)


class BookDeleteAPIView(APIView):
    def delete(self, pk, request):
        try:
            book = Book.objects.get(id=pk)
            book.delete()
            return Response({
                'status': True,
                'message': "Successfully deleted"

            }, status=status.HTTP_200_OK)
        except Exception:
            return Response({
                'status': False,
                'message': "Book is not found"
            }, status=status.HTTP_400_BAD_REQUEST)


class BookUpdateAPIView(APIView):
    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), id=pk)
        data = request.data
        serializer_data = BookSerializer(instance=book, data=data, partial=True)
        if serializer_data.is_valid(raise_exception=True):
            book_saved = serializer_data.save()
        return Response({
            'status': True,
            'message': f"Book {book_saved} update successfully"
        })
