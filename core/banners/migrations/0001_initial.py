# Generated by Django 3.2.5 on 2023-10-25 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pictures', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image_url', models.CharField(blank=True, max_length=256)),
                ('text', models.TextField(blank=True, null=True)),
                ('link', models.TextField(blank=True, max_length=256, null=True)),
                ('type', models.CharField(choices=[('imageBanner', 'картинка'), ('buttonBanner', 'кнопка'), ('titleBanner', 'заголовок'), ('markdownBanner', 'markdown'), ('sliderBanner', 'слайдер')], default='image', max_length=256)),
                ('sort', models.IntegerField(default=0)),
                ('images', models.ManyToManyField(blank=True, related_name='banner_pictures', to='pictures.PictureModel')),
            ],
        ),
    ]
