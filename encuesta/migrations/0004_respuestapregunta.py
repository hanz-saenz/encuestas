# Generated by Django 5.1.3 on 2024-12-05 00:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuesta', '0003_respuesta'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RespuestaPregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta', models.TextField(verbose_name='Respuesta')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateField(auto_now=True, verbose_name='Fecha de actualización')),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encuesta.pregunta')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Respuesta a Preguntas',
                'verbose_name_plural': 'Respuestas a Preguntas',
            },
        ),
    ]
