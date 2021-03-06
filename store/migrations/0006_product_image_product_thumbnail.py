# Generated by Django 4.0.5 on 2022-06-05 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_product_is_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=True, null=True, upload_to='uploads'),
        ),
        migrations.AddField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(default=True, null=True, upload_to='uploads'),
        ),
    ]
