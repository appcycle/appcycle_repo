from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse

from apps.gestaoteste.models import GestaoTeste


class StatusBug (models.Model):
    status_bug = models.CharField(max_length=30, verbose_name=('Status do Bug'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.status_bug

    def get_absolute_url(self):
        return reverse('visualizarstatusbug')



class SeveridadeBug (models.Model):
    severidade_bug = models.CharField(max_length=30, verbose_name=('Severidade do Bug'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.severidade_bug

    def get_absolute_url(self):
        return reverse('visualizarseveridadebug')



class GestaoBug (models.Model):
    codigo_bug = models.CharField(max_length=12, verbose_name=('Código do Bug'))
    nome_bug = models.CharField(max_length=30, verbose_name=('Nome do Bug'))
    desenvolvedor_responsavel = models.CharField(max_length=30, verbose_name=('Desenvolvedor Responsável'))
    relator_bug = models.CharField(max_length=30, verbose_name=('Relator do Bug'))
    ct_relacionado = models.ManyToManyField(GestaoTeste, blank=True, verbose_name='Caso(s) de Teste(s) Relacionado(s)')
    descricao_bug = models.TextField(verbose_name=('Descrição do Bug'), blank=True)
    upload_bug = models.FileField(upload_to='documentos', blank=True, verbose_name=('Evidências'))
    severidade_bug = models.ForeignKey(SeveridadeBug, on_delete=models.PROTECT, null=True, blank=True)
    status_bug = models.ForeignKey(StatusBug, on_delete=models.PROTECT, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_bug

    def get_absolute_url(self):
        return reverse('visualizarbug')
