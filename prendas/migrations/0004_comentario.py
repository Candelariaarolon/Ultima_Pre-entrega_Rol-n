# Generated by Django 5.0.6 on 2024-06-21 20:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prendas', '0003_alter_prendasropa_descripcion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('prenda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='prendas.prendasropa')),
            ],
        ),
    ]
