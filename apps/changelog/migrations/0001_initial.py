# Generated by Django 3.1.2 on 2021-03-09 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Changelog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('versao_changelog', models.IntegerField(verbose_name='Versão')),
                ('data_changelog', models.DateTimeField(verbose_name='Data da Autalização')),
                ('descricao_changelog', models.TextField(verbose_name='Descrição da Atualização')),
            ],
        ),
    ]
