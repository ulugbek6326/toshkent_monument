from django.contrib import admin

from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('img', 'date', 'title', 'description',)
    search_fields = ('title',)
    list_filter = ('title',)


