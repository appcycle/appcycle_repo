from django.db import models

# Create your models here.

class Changelog(models.Model):
    versao_changelog = models.IntegerField(verbose_name=('Versão'))
    data_changelog = models.DateTimeField(verbose_name=('Data da Autalização'))
    descricao_changelog = models.TextField(verbose_name=('Descrição da Atualização'))