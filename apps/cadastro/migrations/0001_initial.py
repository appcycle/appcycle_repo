# Generated by Django 3.1.2 on 2021-06-05 00:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CadastroCliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=70, verbose_name='Nome Completo: ')),
                ('cpf', models.CharField(max_length=20, verbose_name='CPF: ')),
                ('cargo', models.CharField(max_length=20, verbose_name='Cargo: ')),
                ('email', models.EmailField(max_length=30, verbose_name='E-mail: ')),
                ('telefone', models.CharField(max_length=40, verbose_name='Telefone (com DDD): ')),
                ('celular', models.CharField(max_length=40, verbose_name='Celular (com DDD): ')),
                ('nome_empresa', models.CharField(max_length=80, verbose_name='Nome da Empresa: ')),
                ('endereco', models.TextField(verbose_name='Endereço Completo da Empresa: ')),
                ('qtde_usuarios', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Quantidade de usuários: ')),
            ],
        ),
    ]