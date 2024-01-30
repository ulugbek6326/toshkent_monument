from django.http import Http404

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from aboutforme.models import AboutForWe
from aboutforme.serializers import AboutForWeSerializer

from ..pagination import ResultPagination

def get_object(pk, main_class=None):
    try:
        return main_class.objects.get(pk=pk)
    except main_class.DoesNotExist:
        raise Http404("Not found")

class AboutForWeListView(generics.ListAPIView):
    queryset = AboutForWe.objects.all()
    serializer_class = AboutForWeSerializer
    pagination_class = ResultPagination
    
@api_view(['GET'])
def aboutforve_detail(request, pk):
    serializer_class = AboutForWeSerializer
    if request.method == 'GET':
        aboutforwe = get_object(pk,AboutForWe)
        serializer = serializer_class(aboutforwe)
        return Response(serializer.data, status=status.HTTP_200_OK)