from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .aboutforwe import get_object

from contacts.models import Contacts
from contacts.serializers import ContactSerializer

from ..pagination import ResultPagination


class ContactListView(generics.ListAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactSerializer
    pagination_class = ResultPagination
    
    
@api_view(['GET'])
def contact_detail(request, pk):
    serializer_class = ContactSerializer
    if request.method == 'GET':
        contact = get_object(pk,Contacts)
        serializer = serializer_class(contact)
        return Response(serializer.data, status=status.HTTP_200_OK)