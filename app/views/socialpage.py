from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .aboutforwe import get_object

from socialpages.models import SocialPages
from socialpages.serializers import SocialPageSerializer

class SocialPageListView(generics.ListAPIView):
    queryset = SocialPages.objects.all()
    serializer_class = SocialPageSerializer
    
@api_view(['GET'])
def socialpage_detail(request, pk):
    serializer_class = SocialPageSerializer
    if request.method == 'GET':
        socialpage = get_object(pk,SocialPages)
        serializer = serializer_class(socialpage)
        return Response(serializer.data, status=status.HTTP_200_OK)