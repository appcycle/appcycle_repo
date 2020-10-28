# Generated by Django 3.1.2 on 2020-10-25 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0003_projeto_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='deadline',
            field=models.DateField(verbose_name='Deadline'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='dtInicio',
            field=models.DateField(verbose_name='Data de Início'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='nomeProjeto',
            field=models.CharField(max_length=20, verbose_name='Nome do Projeto'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='nomeSprint',
            field=models.CharField(max_length=30, verbose_name='Nome da Sprint'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='status',
            field=models.CharField(max_length=20, verbose_name='Status'),
        ),
    ]
