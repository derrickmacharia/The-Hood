# Generated by Django 3.2.9 on 2022-01-09 17:48

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_hoods_post_hood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighborhood',
            name='hood_image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
    ]