# Generated by Django 4.0.4 on 2022-06-06 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_product_image_product_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default=True, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(default=True, null=True, upload_to='uploads/'),
        ),
    ]
