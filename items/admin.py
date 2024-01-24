from django.contrib import admin
from django.utils.html import format_html

from .models import Items


@admin.register(Items)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('img', 'title', 'description',)
    search_fields = ('title',)
    list_filter = ('title',)
    list_per_page = 25
    list_max_show_all = 100
    
   