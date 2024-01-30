from rest_framework.decorators import api_view
from rest_framework.response import Response

from memory.models import Memory
from items.models import Items
from news.models import News

from scientists.models import Scientists

@api_view(['GET'])
def full_text_search(request):
    data = request.GET.get('search', None)
    return_data = {}
    obj_memorys = Memory.objects.filter(title__icontains=data).values()
    obj_items = Items.objects.filter(title__icontains=data).values()
    obj_news = News.objects.filter(title__icontains=data).values()
    
    return_data['memorys'] = obj_memorys
    return_data['items'] = obj_items
    return_data['news'] = obj_news
    return Response(data=return_data)


@api_view(['GET'])
def max_min_search(request):
    max_data = int(request.GET.get('max_data', 2023))
    min_data = int(request.GET.get('min_data', 0))
    return_data = Scientists.objects.filter(birthday__gte=min_data, birthday__lte=max_data).values()
    return Response(data=return_data)
    
    