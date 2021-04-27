# Generated by Django 3.2 on 2021-04-26 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=15, unique=True, verbose_name='number')),
                ('hardware', models.CharField(max_length=100)),
                ('supplier', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
            ],
            options={
                'verbose_name': 'model',
                'verbose_name_plural': 'models',
                'ordering': ['created'],
            },
        ),
    ]