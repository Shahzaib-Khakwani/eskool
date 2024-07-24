# Generated by Django 4.2 on 2024-07-23 07:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeeParticulars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
                ('prefixAmount', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
    ]
