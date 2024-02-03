from django.db import models

# Create your models here.

class Media(models.Model):
    type = models.CharField(max_length=25, 
                            choices=[
                                ('foto', 'foto'),
                                ('video', 'video'),
                            ], default='foto')
    title = models.CharField(max_length=255)
    foto_video = models.FileField(upload_to='static/image/media_image', blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Media'
        verbose_name_plural = 'Medialar'
        
    def __str__(self):
        return self.title