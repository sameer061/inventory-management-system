# Generated by Django 3.2.6 on 2022-02-21 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_order_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='category',
        ),
    ]
