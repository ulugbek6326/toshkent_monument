from django.db import models
from django.utils.safestring import mark_safe

from ckeditor.fields import RichTextField


# Create your models here.
class AboutForWe(models.Model):
    img = models.ImageField()
    description = RichTextField()
    
    # def admin_photo(self):
    #     return mark_safe('<img src="{}" width="100" height="100" />'.format(self.img.url))
    
    class Meta:
        verbose_name = 'Biz haqimizda'
        verbose_name_plural = 'Biz haqimizda'
        
    def __str__(self):
        return self.description
    
    
class AboutForWeImage(models.Model):
    aboutforwe = models.ForeignKey(AboutForWe, on_delete= models.CASCADE, related_name='aboutforwe_images')
    image = models.ImageField(blank=True, null=True)
    
    
    def __str__(self):
        return self.image.url
    
    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" height="100" />'.format(self.img.url))
    
    admin_photo.short_description = 'Rasm'
    admin_photo.allow_tags = True
        
        
    