from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.

class Contacts(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    description = RichTextField()
    
    
    class Meta:
        verbose_name = 'Kontakt'
        verbose_name_plural = 'Kontaktlar'
        
    def __str__(self):
        return self.full_name