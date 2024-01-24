from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .aboutforwe import get_object

from scientists.models import Scientists
from scientists.serializers import ScientistSerializer

class ScientistListView(generics.ListAPIView):
    queryset = Scientists
    serializer_class = ScientistSerializer
    
    
@api_view(['GET'])
def scientist_detail(request, pk):
    serializer_class = ScientistSerializer
    if request.method == 'GET':
        scientist = get_object(pk,Scientists)
        serializer = serializer_class(scientist)
        return Response(serializer.data, status=status.HTTP_200_OK)