# Generated by Django 5.0.6 on 2024-07-31 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Purchase', '0003_remove_purchasemodel_transaction_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchasemodel',
            name='account',
        ),
    ]
