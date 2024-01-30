from django.contrib import admin
from django.utils.html import format_html

from .models import AboutForWe, AboutForWeImage
# Register your models here.
class AboutForWeImageInline(admin.TabularInline):
    model = AboutForWeImage
    fields = ('image',)
    max_num = 10
    min_num = 1
    can_delete = False
    show_change_link = True
    show_add_button = True
    verbose_name = 'Rasm'
    verbose_name_plural = 'Rasmlar'
    list_display = ('image',)
    ordering = ('image',)
    extra = 0
    

@admin.register(AboutForWe)
class AboutForWeAdmin(admin.ModelAdmin):
    inlines = [AboutForWeImageInline]
    fields= ('description', 'img',)
    list_display = ('display_admin_photo', 'description',)
    list_display_links = ('description',)
    readonly_fields = ('display_admin_photo', 'display_images', )

    
    
    
    def display_admin_photo(self, obj):
        return format_html('<img src="{0}" width="100" height="100"  />'.format(obj.img.url))

    display_admin_photo.short_description = 'Rasm'
    display_admin_photo.allow_tags = True

    def display_images(self, obj):
        images = obj.aboutforwe_images.all()
        return format_html(''.join('<img src="{0}" width="100" height="100" style="margin-right: 10px;"  />'.format(img.image.url) for img in images))

    display_images.short_description = 'Rasm'
    display_images.allow_tags = True
    
    
    def img(self, obj):
        return format_html('<img src="{0}"width="100" height="100" />'.format(obj.img.url))
    
    img.short_description = 'Rasm'
    img.allow_tags = True
