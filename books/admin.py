from django.contrib import admin
from django.utils.html import format_html

from .models import Books


@admin.register(Books)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'book_file')
    search_fields = ('name',)
    list_filter = ('name',)
    list_per_page = 25
    list_max_show_all = 100
