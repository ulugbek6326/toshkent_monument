from django.contrib import admin

from .models import Scientists


@admin.register(Scientists)
class ScientistAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'degree', 'discription',)
    search_fields = ('full_name',)
    list_filter = ('full_name',)


