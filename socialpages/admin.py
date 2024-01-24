from django.contrib import admin

from .models import SocialPages


@admin.register(SocialPages)
class SocialPagesAdmin(admin.ModelAdmin):
    list_display = ('instagram', 'telegram', 'facebook', 'address', 'phone', 'email',)
    


