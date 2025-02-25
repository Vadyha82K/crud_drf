from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from book.models import Book
from book.serializers import BookSerializer


class BookListView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class BookDetailView(APIView):
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, pk):
        book = self.get_object(pk)
        book.delete()
        return Response(status=204)


# @api_view(['GET', 'POST'])
# def books_list(request):
#     if request.method == 'GET':
#         items = Book.objects.all()
#         serializer = BookSerializer(items, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def book_detail(request, pk):
#     try:
#         book = Book.objects.get(pk=pk)
#     except Book.DoesNotExist:
#         return Response(status=404)
#
#     if request.method == 'GET':
#         serializer = BookSerializer(book)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = BookSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         book.delete()
#         return Response(status=204)