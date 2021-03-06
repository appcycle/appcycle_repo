# Generated by Django 3.1.2 on 2021-06-04 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='nomeProjeto',
            field=models.CharField(max_length=20, verbose_name='Nome do Projeto*'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projeto.statusprojeto', verbose_name='Status atual do Projeto'),
        ),
    ]
