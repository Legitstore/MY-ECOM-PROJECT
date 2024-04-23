from django.db import models
from django.contrib.auth.models import User

import datetime
import os
# Create your models here.
def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    filename = "%s.%s" % (nowTime, original_filename)
    return os.path.join('uploads/', filename)

class Category(models.Model):
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    descript = models.TextField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0=default, 1=Hidden")
    # trending = models.BooleanField(default=False, help_text="0=default, 1=Trending")
    # meta_title = models.CharField(max_length=150, null=False, blank=False)
    # meta_keywords = models.CharField(max_length=150, null=False, blank=False)
    # meta_descript = models.TextField(max_length=500, null=False, blank=False)
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    product_image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    small_descript = models.CharField(max_length=250, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    descript = models.TextField(max_length=500, null=False, blank=False)
    original_price = models.FloatField(null=False, blank=False)
    selling_price = models.FloatField(null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0=default, 1=Hidden")
    trending = models.BooleanField(default=False, help_text="0=default, 1=Trending")
    taggings = (
        ('New', 'New'),
        ('Hot', 'Hot'),
        ('New Arrival', 'New Arrival'),
        ('Used', 'Used'),
        ('Refurbished', 'Refurbished'),
    )
    tag = models.CharField(max_length=150, choices=taggings, null=False, blank=False)
    meta_title = models.CharField(max_length=150, null=False, blank=False)
    meta_descript = models.TextField(max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    @property
    def prod_imageURL(self):
        try:
            url = self.product_image.url
        except:
            url = ''
        return url