# Generated by Django 3.2.5 on 2023-10-28 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_pluginmodel_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='plugins',
            field=models.ManyToManyField(to='orders.PluginModel'),
        ),
    ]
