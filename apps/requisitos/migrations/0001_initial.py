# Generated by Django 3.1.2 on 2020-10-25 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projeto', '0004_auto_20201025_1705'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Requisito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeRequisito', models.CharField(max_length=30, verbose_name='Nome do Requisito')),
                ('responsavel', models.CharField(max_length=30, verbose_name='Responsável pelo Desenvolvimento')),
                ('código', models.CharField(max_length=20, verbose_name='Código do Requisito')),
                ('prioridade', models.CharField(max_length=10, verbose_name='Prioridade do Requisito')),
                ('risco', models.CharField(max_length=10, verbose_name='Risco do Requisito')),
                ('motivo', models.CharField(max_length=20, verbose_name='Motivo do Requisito')),
                ('requisitosImpactados', models.CharField(max_length=100, verbose_name='Requisitos Impactados')),
                ('estoriaUsuario', tinymce.models.HTMLField()),
                ('regrasNegocio', tinymce.models.HTMLField()),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projeto.projeto')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
