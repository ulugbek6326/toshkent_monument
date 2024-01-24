from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .aboutforwe import get_object

from media.models import Media
from media.serializers import MediaSerializer


class MediaListView(generics.ListAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('type', openapi.IN_QUERY, description='Filter by type', type=openapi.TYPE_STRING),
        ]
    )
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
@api_view(['GET'])
def media_detail(request, pk):
    serializer_class = MediaSerializer
    if request.method == 'GET':
        media = get_object(pk,Media)
        serializer = serializer_class(media)
        return Response(serializer.data, status=status.HTTP_200_OK)