# Generated by Django 3.2.5 on 2023-10-27 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_ordermodel_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='PluginModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('per_photo', models.FloatField()),
                ('link', models.URLField()),
            ],
        ),
    ]
