from django.db import models
from django.utils import timezone

from ckeditor.fields import RichTextField

# Create your models here.

class News(models.Model):
    img = models.ImageField(upload_to='static/image/new_image')
    date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=255)
    description = RichTextField()
    
    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'
        
    def __str__(self):
        return self.title