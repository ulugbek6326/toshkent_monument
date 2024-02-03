from django.contrib import admin
from django.utils.html import format_html
from aboutforme.models import AboutForWe, AboutForWeImage


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
    list_display = ('img',)
    ordering = ('image',)
    extra = 0


@admin.register(AboutForWe)
class AboutForWeAdmin(admin.ModelAdmin):
    inlines = [AboutForWeImageInline]
    list_display = ('display_admin_photo', 'display_images',)
    search_fields = ('description',)
    list_filter = ('description',)
    list_per_page = 25
    list_max_show_all = 100
    save_as = False
    save_as_continue = True
    save_on_top = False
    readonly_fields = ('display_admin_photo', 'display_images',)

    def display_admin_photo(self, obj):
        return format_html('<img src="{0}" width="100" height="100" />'.format(obj.img.url))

    display_admin_photo.short_description = 'Rasm'
    display_admin_photo.allow_tags = True

    def display_images(self, obj):
        images = obj.aboutforwe_images.all()
        return format_html(''.join('<img src="{0}" width="100" height="100" style="margin-right: 10px;" />'.format(img.image.url) for img in images))

    display_images.short_description = 'Images'
    display_images.allow_tags = True





# from django.contrib import admin
# from django.utils.html import format_html
# from django.utils.safestring import mark_safe
#
# from .models import AboutForWe, AboutForWeImage
# # Register your models here.
#
#
# class AboutForWeImageInline(admin.TabularInline):
#     model = AboutForWeImage
#     fields = ('image',)
#     max_num = 10
#     min_num = 1
#     can_delete = False
#     show_change_link = True
#     show_add_button = True
#     verbose_name = 'Rasm'
#     verbose_name_plural = 'Rasmlar'
#     list_display = ('image',)
#     ordering = ('image',)
#     extra = 0
#
#
# @admin.register(AboutForWe)
# class AboutForWeAdmin(admin.ModelAdmin):
#     inlines = [AboutForWeImageInline]
#     fields = ('description', 'img', 'admin_photo',)
#     list_display = ('admin_photo',)
#     list_display_links = ('admin_photo',)
#     readonly_fields = ('admin_photo',)
#
#     def logo_image(self, obj):
#         return format_html('<img src="{0}" width="100" height="100" />'.format(obj.logo_image.url))
#
#     logo_image.short_description = 'Rasm'
#     logo_image.allow_tags = True
#
#     def admin_photo(self, obj):
#         return format_html('<img src="{0}" width="100" height="100"  />'.format(obj.img.url))
#
#     admin_photo.short_description = 'Rasm'
#     admin_photo.allow_tags = True
#
#     def display_images(self, obj):
#         images = obj.aboutforwe_images.all()
#         return format_html(''.join('<img src="{0}" width="100" height="100" style="margin-right: 10px;"  />'.format(img.image.url) for img in images))
#
#     display_images.short_description = 'Rasm'
#     display_images.allow_tags = True
#
#     def img(self, obj):
#         return format_html('<img src="{0}"width="100" height="100" />'.format(obj.img.url))
#
#     img.short_description = 'img'
#     img.allow_tags = True
