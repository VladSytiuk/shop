# Generated by Django 3.2.3 on 2021-05-21 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Product name')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='image')),
                ('description', models.TextField(null=True, verbose_name='description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='price')),
                ('diagonal', models.CharField(max_length=255, verbose_name='Screen diagonal')),
                ('display_type', models.CharField(max_length=255, verbose_name='display matrix type')),
                ('resolution', models.CharField(max_length=255, verbose_name='Resolution')),
                ('battery_volume', models.CharField(max_length=255, verbose_name='Battery volume')),
                ('ram', models.CharField(max_length=255, verbose_name='RAM')),
                ('sd', models.BooleanField(default=True)),
                ('sd_memory_max', models.CharField(max_length=255, verbose_name='Maximum memory capacity')),
                ('main_cam_mp', models.CharField(max_length=255, verbose_name='Main camera')),
                ('front_cam_mp', models.CharField(max_length=255, verbose_name='Front camera')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Product name')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='image')),
                ('description', models.TextField(null=True, verbose_name='description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='price')),
                ('diagonal', models.CharField(max_length=255, verbose_name='Screen diagonal')),
                ('display_type', models.CharField(max_length=255, verbose_name='display matrix type')),
                ('processor_freq', models.CharField(max_length=255, verbose_name='Processor frequency')),
                ('ram', models.CharField(max_length=255, verbose_name='RAM')),
                ('video', models.CharField(max_length=255, verbose_name='Video card')),
                ('time_without_charge', models.CharField(max_length=255, verbose_name='Time-running without charging')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]