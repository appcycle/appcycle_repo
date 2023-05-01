# Generated by Django 3.1.2 on 2021-03-09 20:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projeto', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PrioridadeRequisito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prioridade_requisito', models.CharField(blank=True, max_length=20, verbose_name='Prioridade do Requisito')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StatusRequisito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_requisito', models.CharField(blank=True, max_length=20, verbose_name='Status do Requisito')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RiscoRequisito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risco_requisito', models.CharField(blank=True, max_length=20, verbose_name='Risco do Requisito')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Requisito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeRequisito', models.CharField(max_length=30, verbose_name='Nome do Requisito')),
                ('responsavel', models.CharField(blank=True, max_length=30, null=True, verbose_name='Responsável pelo Desenvolvimento')),
                ('codigo', models.CharField(max_length=20, verbose_name='Código do Requisito')),
                ('ponto_focal', models.CharField(blank=True, max_length=20, null=True, verbose_name='Ponto Focal')),
                ('motivo', models.CharField(blank=True, max_length=100, null=True, verbose_name='Motivo do Requisito')),
                ('urlRepositorio', models.URLField(blank=True, null=True, verbose_name='URL no Repositório')),
                ('urlJira', models.URLField(blank=True, null=True, verbose_name='URL no JIRA')),
                ('storypoints', models.CharField(blank=True, max_length=3, null=True, verbose_name='Story Points')),
                ('requisitosImpactados', models.TextField(blank=True, null=True, verbose_name='Requisitos Impactados')),
                ('documento', models.FileField(blank=True, null=True, upload_to='documentos')),
                ('estoriaUsuario', models.TextField(blank=True, null=True, verbose_name='Estória do Usuário')),
                ('regrasNegocio', models.TextField(blank=True, null=True, verbose_name='Regras de Negócios')),
                ('prioridade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='requisitos.prioridaderequisito')),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projeto.projeto')),
                ('risco', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='requisitos.riscorequisito')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='requisitos.statusrequisito')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
