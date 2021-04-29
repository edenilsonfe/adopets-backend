# Generated by Django 3.2 on 2021-04-22 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razao_social', models.CharField(max_length=100)),
                ('cnpj', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=50)),
                ('telefone', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=100)),
            ],
        ),
    ]
