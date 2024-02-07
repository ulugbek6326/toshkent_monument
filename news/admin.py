from django.contrib import admin

from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('img', 'date', 'title', 'description',)
    fields = ('img', 'date', 'title_uz', 'title_ru', 'title_en', 'description_uz', 'description_ru', 'description_en',)
    search_fields = ('title',)
    list_filter = ('title',)


