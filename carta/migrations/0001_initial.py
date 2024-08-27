# Generated by Django 5.1 on 2024-08-27 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('descripcion', models.CharField(default='', max_length=400)),
                ('img', models.URLField()),
            ],
        ),
    ]
