from django.db import models

class Acesso(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=5)
    data_acesso = models.DateTimeField(auto_now_add=True)

    def __clstr__(self):
        return f"{self.nome} - {self.matricula}"
    
class MatriculaAutorizada(models.Model):
    numero = models.CharField(max_length=5, unique=True, verbose_name="Matrícula Permitida")
    nome_aluno = models.CharField(max_length=100, blank=True, help_text="Opcional: Nome para seu controle")

    def __str__(self):
        return f"{self.numero} - {self.nome_aluno}"