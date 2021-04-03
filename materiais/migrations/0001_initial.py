# Generated by Django 3.1.7 on 2021-04-02 22:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ListaMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Atualizado em')),
                ('status', models.BooleanField(default=True)),
                ('lapis', models.PositiveIntegerField(default=0, verbose_name='Lápis')),
                ('caderno', models.PositiveIntegerField(default=0, verbose_name='Caderno')),
                ('canetas', models.PositiveIntegerField(default=0, verbose_name='Canetas')),
                ('borracha', models.PositiveIntegerField(default=0, verbose_name='Borracha')),
                ('lapis_cor', models.PositiveIntegerField(default=0, verbose_name='Lápis de Cor')),
                ('tesoura', models.PositiveIntegerField(default=0, verbose_name='Tesoura')),
                ('mochila', models.PositiveIntegerField(default=0, verbose_name='Mochila')),
                ('nome', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Lista de Material',
                'verbose_name_plural': 'Lista de Materiais',
            },
        ),
    ]
