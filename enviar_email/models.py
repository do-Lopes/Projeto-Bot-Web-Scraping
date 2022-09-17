from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length = 200)
    link = models.URLField(max_length=200)
    lingua = models.CharField(max_length = 50, blank=True, null = True)
    filter = models.CharField(max_length = 80, blank=True, null = True)
    region = models.CharField(max_length = 30, blank=True, null = True)

    def __str__(self) -> str:
        return self.titulo