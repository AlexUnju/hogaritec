# Generated by Django 5.1.2 on 2024-11-15 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0010_alter_sale_options_sale_reference_sale_status_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sale',
            options={'ordering': ['-date'], 'verbose_name': 'Sale', 'verbose_name_plural': 'Ventas'},
        ),
    ]
