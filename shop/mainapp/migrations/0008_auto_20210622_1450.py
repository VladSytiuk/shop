# Generated by Django 3.2.3 on 2021-06-22 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_order_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notebook',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='image'),
        ),
    ]