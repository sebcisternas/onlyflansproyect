# Generated by Django 4.2 on 2024-04-23 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_remove_carrito_flanes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemcarrito',
            name='carrito',
        ),
        migrations.RemoveField(
            model_name='itemcarrito',
            name='flan',
        ),
        migrations.DeleteModel(
            name='Carrito',
        ),
        migrations.DeleteModel(
            name='ItemCarrito',
        ),
    ]
