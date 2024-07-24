# Generated by Django 4.2 on 2024-07-23 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
        ('eClass', '0001_initial'),
        ('myapp', '0002_feeparticulars'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeparticulars',
            name='fee_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eClass.eclass'),
        ),
        migrations.AddField(
            model_name='feeparticulars',
            name='students',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.student'),
        ),
    ]