from rest_framework.pagination import PageNumberPagination
from rest_framework .response import Response


class ResultPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'limit'
    max_page_size = 1000
    filters = None
    
    def get_paginated_response(self, data):
        page_size = int(self.request.query_params.get('limit',self.page_size))
        return Response({
            'pagination': {
               'currentPage': self.page.number,
                'lastPage': self.page.paginator.num_pages,
                'perPage': page_size,
                'total': self.page.paginator.count, 
            },
            'results': data,
            'filters': self.filters
        })
        
    @classmethod
    def set_filter(cls, filters):
        cls.filters = filters
        

class LargeResultSetPagination(ResultPagination):
    page_size = 1000