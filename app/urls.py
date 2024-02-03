from django.conf.urls.static import static
from django.urls import path

from config import settings
from .views.aboutforwe import AboutForWeListView, aboutforve_detail
from .views.book import BookListView, book_detail
from .views.contact import ContactListView, contact_detail
from .views.item import ItemListView, item_detail
from .views.media import MediaListView, media_detail
from .views.memory import MemoryListView, memory_detail
from .views.new import NewListView, new_detail
from .views.scientist import ScientistListView, scientist_detail
from .views.socialpage import SocialPageListView, socialpage_detail
from.views.full_text_search import full_text_search, max_min_search

urlpatterns = [
    path('aboutforwe/', AboutForWeListView.as_view(), name='aboutforwe'),
    path('aboutforwe_detail/<int:pk>/', aboutforve_detail, name='aboutforwe_detail'),
    
    path('book/', BookListView.as_view(), name='book'),
    path('book_detail/<int:pk>/', book_detail, name='book_detail'),
    
    path('contact/', ContactListView.as_view(), name='contact'),
    path('contact_detail/<int:pk>/', contact_detail, name='contact_detail'),
    
    path('item/', ItemListView.as_view(), name='item'),
    path('item_detail/<int:pk>/', item_detail, name='item_detail'),
    
    path('media/', MediaListView.as_view(), name='media'),
    path('media_detail/<int:pk>/', media_detail, name='media_detail'),
    
    path('memory/', MemoryListView.as_view(), name='memory'),
    path('memory_detail/<int:pk>/', memory_detail, name='memory_detail'),
    
    path('new/', NewListView.as_view(), name='new'),
    path('new_detail/<int:pk>', new_detail, name='new_detail'),
    
    path('scientist/',ScientistListView.as_view(), name='scientist'),
    path('scientist_detail/<int:pk>',scientist_detail, name='scientist_detail'),
    
    path('socialpage/',SocialPageListView.as_view(), name='socialpage'),
    path('socialpage_detail/<int:pk>', socialpage_detail, name='socialpage_detail'),
    
    path('search/', full_text_search, name='search'),
    path('max_min_search/', max_min_search, name='max_min_search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)