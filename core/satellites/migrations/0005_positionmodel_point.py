# Generated by Django 3.2.5 on 2023-10-27 18:49

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('satellites', '0004_auto_20231027_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='positionmodel',
            name='point',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
    ]