# Generated by Django 3.1.7 on 2021-04-07 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20210407_2120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='variant',
        ),
        migrations.RemoveField(
            model_name='shopcart',
            name='variant',
        ),
    ]
