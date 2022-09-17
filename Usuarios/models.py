from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100)
    senha = models.CharField(max_length = 100)
    lingua = models.CharField(max_length = 300, blank=True, null = True)
    region = models.CharField(max_length = 300, blank=True, null = True)
    filtro = models.CharField(max_length = 300, blank=True, null = True)

    def __str__(self) -> str:
        return self.email
