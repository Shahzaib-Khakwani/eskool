# Generated by Django 4.2 on 2024-07-28 13:40

from django.db import migrations, models
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_accountsettings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountsettings',
            name='currency',
            field=models.CharField(default='$', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='accountsettings',
            name='timezone',
            field=timezone_field.fields.TimeZoneField(default='UTC', null=True),
        ),
    ]
