from django.db import models

# Create your models here.
class Post(models.Model):
    
    titulo = models.CharField(max_length=30)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='blog/images', null=True, blank=True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.titulo