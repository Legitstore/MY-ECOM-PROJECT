# Generated by Django 4.2.7 on 2024-04-19 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_product_product_image1_product_product_image2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='meta_descript',
        ),
        migrations.RemoveField(
            model_name='product',
            name='meta_title',
        ),
    ]
