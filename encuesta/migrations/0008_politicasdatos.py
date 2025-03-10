# Generated by Django 5.1.3 on 2024-12-13 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuesta', '0007_alter_calificacion_calificacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='PoliticasDatos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Título')),
                ('archivo', models.FileField(upload_to='static/assets/imagenes/politicas/', verbose_name='Archivo')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
            ],
            options={
                'verbose_name': 'Política de Datos',
                'verbose_name_plural': 'Políticas de Datos',
            },
        ),
    ]
