from django.db import models

# Create your models here.

class Books(models.Model):
    name = models.CharField(max_length=255)
    book_file = models.FileField()
    
    class Meta:
        verbose_name = 'Elektron adabiyot'
        verbose_name_plural = 'Elektron adabiyotlar'
        
    def __str__(self):
        return self.name