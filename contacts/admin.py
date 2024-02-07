from django.contrib import admin
from django.utils.html import format_html

from .models import Contacts


@admin.register(Contacts)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'description')
    fields = ('full_name', 'email', 'description_uz', 'description_ru', 'description_en',)
    search_fields = ('full_name',)
    list_filter = ('full_name',)
    list_per_page = 25
    list_max_show_all = 100
    