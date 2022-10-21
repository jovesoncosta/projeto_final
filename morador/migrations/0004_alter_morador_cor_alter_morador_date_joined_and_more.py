# Generated by Django 4.1.2 on 2022-10-21 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('morador', '0003_remove_morador_certnascimento_morador_date_joined_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='morador',
            name='cor',
            field=models.CharField(choices=[('indigena', 'Indigena'), ('Branca', 'Branca'), ('Amarelo', 'Amarela'), ('Parda', 'Parda'), ('Negra', 'Negro/Preta')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='morador',
            name='date_joined',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='morador',
            name='sexo',
            field=models.CharField(choices=[('M', 'MASCULINO'), ('F', 'FEMININO')], max_length=10, null=True),
        ),
    ]
