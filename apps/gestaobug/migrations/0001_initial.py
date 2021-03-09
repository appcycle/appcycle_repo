# Generated by Django 3.1.2 on 2021-03-09 20:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestaoteste', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusBug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_bug', models.CharField(max_length=30, verbose_name='Status do Bug')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SeveridadeBug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('severidade_bug', models.CharField(max_length=30, verbose_name='Severidade do Bug')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GestaoBug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_bug', models.CharField(max_length=12, verbose_name='Código do Bug')),
                ('nome_bug', models.CharField(max_length=30, verbose_name='Nome do Bug')),
                ('desenvolvedor_responsavel', models.CharField(max_length=30, verbose_name='Desenvolvedor Responsável')),
                ('relator_bug', models.CharField(max_length=30, verbose_name='Relator do Bug')),
                ('descricao_bug', models.TextField(blank=True, verbose_name='Descrição do Bug')),
                ('upload_bug', models.FileField(blank=True, upload_to='documentos', verbose_name='Evidências')),
                ('ct_relacionado', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='gestaoteste.gestaoteste', verbose_name='Caso de Teste Relacionado')),
                ('severidade_bug', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='gestaobug.severidadebug')),
                ('status_bug', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='gestaobug.statusbug')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
