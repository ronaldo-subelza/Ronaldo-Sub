# Generated by Django 5.1.2 on 2024-10-27 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ropa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenda', models.CharField(max_length=15)),
                ('marca', models.CharField(max_length=15)),
                ('talla', models.IntegerField()),
            ],
        ),
    ]
