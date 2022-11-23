from tabnanny import verbose
from unittest.mock import DEFAULT
from django.db import models

# Create your models here.
SEXO_CHOICES = [
    ('M','Masculino'),
    ('F', 'Feminino')
]

CURSO_CHOICES = [
    ('Curso Técnico','Curso Técnico'),
    ('Curso Superior','Curso Superior')
]

class Minicurso(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome


class Curso(models.Model):
    nome = models.CharField(max_length=150)
    grau = models.CharField(
        max_length=100,
        choices = CURSO_CHOICES
    )

    def __str__(self):
        return self.grau

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    email = models.EmailField()
    data_nascimento = models.DateField()
    sexo = models.CharField(
        max_length=100,
        choices= SEXO_CHOICES,
        default='FEMININO'
    )   

    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    minicursos = models.ManyToManyField(Minicurso)
    
    def __str__(self):
        return self.nome