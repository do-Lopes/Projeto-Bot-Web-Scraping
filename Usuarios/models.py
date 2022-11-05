from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100)
    senha = models.CharField(max_length = 100)
    region = models.TextField(max_length = 300, blank=True, null = True, default="['pt BR']")
    filtro = models.TextField(max_length = 300, blank=True, null = True)

    def __str__(self) -> str:
        return self.email
