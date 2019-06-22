from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from appefirst import models



class MainPageView(LoginRequiredMixin, View):
    def get(self, request):
        country = models.Country.objects.all()
        ctx = {"country": country}
        return render(request, 'appefirst/index.html', ctx)


class ProductView(LoginRequiredMixin, View):
    def get(self, request, id):
        product = models.Products.objects.get(id=id)
        domain = "http://healthy-now-nature.com/"
        ctx = {"prod": product,
               "domain": domain}
        return render(request, 'appefirst/prod_det.html', ctx)
