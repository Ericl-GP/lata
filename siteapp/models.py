from django.db import models

#-------------------------------
"""
class banner(models.Model):
    image=models.ImageField(upload_to='banner/')
    cria=models.DateTimeField(auto_now_add=True)

class links(models.Model):
    titulo=models.CharField(max_length=100)
    link=models.URLField
    cria=models.DateTimeField(auto_now_add=True)

class conteudo(models.Model):
    titulo=models.CharField(max_length=100)
    conteudo=models.TextField()
    cria=models.DateTimeField(auto_now_add=True)

class Accordion(models.Model):
    titulo=models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_nome='post'
        verbose_nome_plural='post'
        ordering=['id']
"""

class Posts(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self): # adicionar isso
        return self.title
    
    class Meta:  # adicionar isso
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['id']