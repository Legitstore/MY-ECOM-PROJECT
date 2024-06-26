# Generated by Django 4.2.7 on 2024-04-19 21:18

from django.db import migrations, models
import django.db.models.deletion
import events.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_category_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to=events.models.get_file_path)),
                ('small_descript', models.CharField(max_length=250)),
                ('quantity', models.IntegerField()),
                ('descript', models.TextField(max_length=500)),
                ('original_price', models.FloatField()),
                ('selling_price', models.FloatField()),
                ('status', models.BooleanField(default=False, help_text='0=default, 1=Hidden')),
                ('trending', models.BooleanField(default=False, help_text='0=default, 1=Trending')),
                ('tag', models.CharField(choices=[('New', 'New'), ('Hot', 'Hot'), ('New Arrival', 'New Arrival'), ('Used', 'Used'), ('Refurbished', 'Refurbished')], max_length=150)),
                ('meta_title', models.CharField(max_length=150)),
                ('meta_descript', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.category')),
            ],
        ),
    ]
