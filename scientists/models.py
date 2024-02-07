from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.

class Scientists(models.Model):
    full_name = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    discription = RichTextField()
    birthday = models.DateField()
    diedday = models.DateField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Olim'
        verbose_name_plural = 'Olimlar'
        
    def __str__(self):
        return self.full_name