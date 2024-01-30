from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.

class Memory(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='static/image/memory_image')
    description = RichTextField()
    like = models.PositiveIntegerField(default=0, blank=True, null=True)
    file = models.FileField(upload_to='static/image/memory_image')
    longitude = models.FloatField()
    latitude = models.FloatField()
    
    class Meta:
        verbose_name = 'Arxiologik'
        verbose_name_plural = 'Arxiologik'
        
    def __str__(self):
        return self.title