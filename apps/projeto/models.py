from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from tinymce import models as tinymce_models
from tinymce.models import HTMLField

class StatusProjeto(models.Model):
    statusprojeto = models.CharField(max_length=20, verbose_name=('Status do Projeto'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.statusprojeto

    def get_absolute_url(self):
        return reverse('visualizarstatusprojeto')


class Projeto(models.Model):
    nomeProjeto = models.CharField(max_length=20, verbose_name=('Nome do Projeto*'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.TextField(verbose_name='Descrição do Projeto', null=True, blank=True)
    dtInicio = models.DateField(auto_now=False, auto_now_add=False, verbose_name=('Data de Início'), null=True, blank=True)
    deadline = models.DateField(auto_now=False, auto_now_add=False, verbose_name=('Deadline'), null=True, blank=True)
    nomeSprint = models.CharField(max_length=30, verbose_name=('Nome da Sprint'), null=True, blank=True)
    status = models.ForeignKey(StatusProjeto, on_delete=models.CASCADE, verbose_name=('Status atual do Projeto'))

    def __str__(self):
        return self.nomeProjeto

    def get_absolute_url(self):
        return reverse('search_projeto')


