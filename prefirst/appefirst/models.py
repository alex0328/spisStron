from django.db import models

# Create your models here.


PAGE_TYPE_CHOICES = [
    ('lp', 'landing'),
    ('pre', 'prelanding'),
    ('off', 'official'),
    ('oth', 'other'),
]

DOMAINS_OWNERS = [
    ('affbay', "affbay"),
    ('zenia', "zenia"),
    ('natalia', "natalia"),
    ('user1', "user1"),
    ('user2', "user2"),
    ('user3', "user3"),
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
    product_is_test = models.BooleanField(default=True)
    product_is_sell = models.BooleanField(default=True)
    product_is_smth = models.BooleanField(default=True)
    product_notes = models.CharField(max_length=300, default=None)


    def __str__(self):
        return "{} {}".format(self.product_name, self.product_country)

class Pages(models.Model):
    page_type = models.CharField(choices=PAGE_TYPE_CHOICES, max_length=30)
    page_number = models.CharField(max_length=10, unique=False)
    page_code = models.CharField(max_length=64)
    page_url = models.CharField(max_length=300)
    page_product = models.ForeignKey(Products, on_delete=models.PROTECT)
    page_project_code = models.CharField(max_length=64)
    page_is_finished = models.BooleanField(default=False)
    page_is_in_affbay = models.BooleanField(default=False)
    page_is_smth1 = models.BooleanField(default=False)
    page_is_smth2 = models.BooleanField(default=False)
    page_notes1 = models.CharField(max_length=200, default=None)
    page_notes2 = models.CharField(max_length=200, default=None)

class Domains(models.Model):
    domain_name = models.CharField(max_length=64, default=None)
    domain_token = models.CharField(max_length=64, default=None)
    domain_owner = models.CharField(choices=DOMAINS_OWNERS, max_length=30)

    def __str__(self):
        return "{} {}".format(self.page_type, self.page_product)