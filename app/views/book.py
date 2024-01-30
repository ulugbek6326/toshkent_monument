from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .aboutforwe import get_object

from books.models import Books
from books.serializers import BookSerializer

from ..pagination import ResultPagination


class BookListView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    pagination_class = ResultPagination
    
    
@api_view(['GET'])
def book_detail(request, pk):
    serializer_class = BookSerializer
    if request.method == 'GET':
        book = get_object(pk,Books)
        serializer = serializer_class(book)
        return Response(serializer.data, status=status.HTTP_200_OK)