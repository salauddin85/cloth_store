# Generated by Django 5.0.6 on 2024-08-01 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cloth_product', '0016_alter_wishlist_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-price']},
        ),
    ]
