from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from tinymce import models as tinymce_models
from tinymce.models import HTMLField


class Projeto(models.Model):
    nomeProjeto = models.CharField(max_length=20, verbose_name=('Nome do Projeto'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = HTMLField()
    dtInicio = models.DateField(auto_now=False, auto_now_add=False, verbose_name=('Data de Início'))
    deadline = models.DateField(auto_now=False, auto_now_add=False, verbose_name=('Deadline'))
    nomeSprint = models.CharField(max_length=30, verbose_name=('Nome da Sprint'))
    status = models.CharField(max_length=20, verbose_name=('Status'))


    def __str__(self):
        return self.nomeProjeto


    def get_absolute_url(self):
        return reverse('visualizarProjeto')
