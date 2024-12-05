from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto_perfil = models.ImageField(upload_to='perfil/', null=True, blank=True)
    data_conclusao = models.DateField(null=True, blank=True)
    genero = models.CharField(max_length=10, choices=[('masculino', 'Masculino'), ('feminino', 'Feminino'), ('outro', 'Outro'), ('nao_dizer', 'Prefiro não dizer')], default='nao_dizer')
    campus = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    nivel = models.CharField(max_length=20, choices=[('usuario', 'Visitante'), ('editor', 'Egressos'), ('administrador', 'Administrador')], default='usuario')

    def __str__(self):
        return self.user.username
