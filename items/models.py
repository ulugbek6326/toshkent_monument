from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.

class Items(models.Model):
    img = models.ImageField(upload_to='static/image/item_image')
    title = models.CharField(max_length=255)
    description = RichTextField()
    
    class Meta:
        verbose_name = 'Ashyolar'
        verbose_name_plural = 'Ashyolar'
        
    def __str__(self):
        return self.title