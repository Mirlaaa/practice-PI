# Generated by Django 4.1.2 on 2022-11-23 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudo_forms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], default='FEMININO', max_length=100),
        ),
    ]
