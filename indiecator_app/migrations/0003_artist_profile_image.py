# Generated by Django 3.0.6 on 2020-05-24 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indiecator_app', '0002_auto_20200524_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='indiecator/'),
        ),
    ]
