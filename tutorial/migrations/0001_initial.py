# Generated by Django 5.1.6 on 2025-02-10 17:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_colaborator', models.IntegerField()),
                ('first_colaborator', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('name_allie', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OnlyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.TextField(blank=True, null=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('technologies', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Proyect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('technologies', models.CharField(max_length=255)),
                ('allie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tutorial.allies')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.IntegerField()),
                ('date', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('emprise', models.CharField(max_length=100)),
                ('proyect_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tutorial.proyect')),
            ],
        ),
    ]
