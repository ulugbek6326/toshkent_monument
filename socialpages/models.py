from django.db import models

# Create your models here.

class SocialPages(models.Model):
    instagram = models.CharField(max_length=255)
    telegram = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=14)
    email = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Ijtimoiy Sahifa'
        verbose_name_plural = 'Ijtimoiy Sahifalar'
        
    def __str__(self):
        return self.address