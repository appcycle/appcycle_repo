# Generated by Django 3.1.2 on 2021-03-07 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0003_auto_20210116_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='descricao',
            field=models.TextField(blank=True, null=True, verbose_name='Descrição do Projeto'),
        ),
    ]