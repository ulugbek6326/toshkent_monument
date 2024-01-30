from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .aboutforwe import get_object

from memory.models import Memory
from memory.serializers import MemorySerializer

from ..pagination import ResultPagination


class MemoryListView(generics.ListAPIView):
    queryset = Memory.objects.all()
    serializer_class = MemorySerializer
    pagination_class = ResultPagination
    

@api_view(['GET'])
def memory_detail(request, pk):
    serializer_class = MemorySerializer
    if request.method == 'GET':
        memory = get_object(pk,Memory)
        serializer = serializer_class(memory)
        return Response(serializer.data, status=status.HTTP_200_OK)
