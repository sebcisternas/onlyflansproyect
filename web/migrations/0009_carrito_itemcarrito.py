# Generated by Django 4.2 on 2024-04-23 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0008_remove_itemcarrito_carrito_remove_itemcarrito_flan_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ItemCarrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.carrito')),
                ('flan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.flan')),
            ],
        ),
    ]
