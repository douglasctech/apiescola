from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    rg = models.CharField(max_length=9)

    def __str__(self):
        return self.nome

class Professor(models.Model):
    nome = models.CharField(max_length=50)
    rg = models.CharField(max_length=9)

    def __str__(self):
        return self.nome    
    
 

