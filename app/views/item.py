from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .aboutforwe import get_object

from items.models import Items
from items.serializers import ItemSerializer

from ..pagination import ResultPagination


class ItemListView(generics.ListAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer
    pagination_class = ResultPagination
    
    
@api_view(['GET'])
def item_detail(request, pk):
    serializer_class = ItemSerializer
    if request.method == 'GET':
        item = get_object(pk,Items)
        serializer = serializer_class(item)
        return Response(serializer.data, status=status.HTTP_200_OK)