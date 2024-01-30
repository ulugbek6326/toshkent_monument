from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .aboutforwe import get_object

from news.models import News
from news.serializers import NewsSerializer

from ..pagination import ResultPagination


class NewListView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = ResultPagination
    
@api_view(['GET'])
def new_detail(request, pk):
    serializer_class = NewsSerializer
    if request.method == 'GET':
        new = get_object(pk,News)
        serializer = serializer_class(new)
        return Response(serializer.data, status=status.HTTP_200_OK)