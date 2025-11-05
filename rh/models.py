from django.db import models

# Create your models here.
class Funcionarios(models.Model):
    foto = models.ImageField(null=True, blank=True)
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    data_contratacao = models.DateField()
    status = models.BooleanField(default=True)
    
    #corrige o problema de duplo 's' no nome do modelo no admin
    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários" # Define o nome plural correto
    def __str__(self):
        return self.nome