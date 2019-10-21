from django.contrib import admin
from appefirst.models import Products,Pages,Country,Domains, LottoNumbers

# Register your models here.
admin.site.register(Products)
admin.site.register(Pages)
admin.site.register(Country)
admin.site.register(Domains)
admin.site.register(LottoNumbers)

