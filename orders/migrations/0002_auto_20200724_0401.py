# Generated by Django 2.0.3 on 2020-07-24 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='toppings',
        ),
        migrations.RemoveField(
            model_name='subs',
            name='toppings',
        ),
    ]
