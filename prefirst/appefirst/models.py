from django.db import models

# Create your models here.


PAGE_TYPE_CHOICES = [
    ('lp', 'landing'),
    ('pre', 'prelanding'),
    ('off', 'official'),
    ('oth', 'other'),
]

class Country(models.Model):
    country_name = models.CharField(max_length=64, unique=True)
    country_code = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.country_name

class Products(models.Model):
    product_name = models.CharField(max_length=64)
    product_country = models.ForeignKey(Country, on_delete=models.PROTECT)
    product_price = models.IntegerField()
    product_epic = models.CharField(max_length=64)
    product_sku = models.CharField(max_length= 200, unique=True)
    product_desc = models.CharField(max_length=300)
    product_is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{} {}".format(self.product_name, self.product_country)

class Pages(models.Model):
    page_type = models.CharField(choices=PAGE_TYPE_CHOICES, max_length=30)
    page_code = models.CharField(max_length=64)
    page_url = models.CharField(max_length=300)
    page_product = models.ForeignKey(Products, on_delete=models.PROTECT)
    page_project_code = models.CharField(max_length=64)

    def __str__(self):
        return "{} {}".format(self.page_type, self.page_product)