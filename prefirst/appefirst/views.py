from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from appefirst import models
import requests



class MainPageView(LoginRequiredMixin, View):
    def get(self, request):
        country = models.Country.objects.all()
        ctx = {"country": country}
        return render(request, 'appefirst/index.html', ctx)

class DBDView(LoginRequiredMixin, View):
    def get(self, request):
        url = 'http://serwis.mobilotto.pl/mapi_v6/index.php?json=getLotto'
        req = requests.get(url).json()
        num_losowania = req['num_losowania']
        numerki_tosort = req['numerki']
        numery_order = numerki_tosort.split(',')
        numerki_tosort = []
        for i in numery_order:
            if int(i)<10:
                i = "0"+i
            numerki_tosort.append(i)
        data_losowania_raw = req['data_losowania']
        cut = data_losowania_raw.split(' ')
        data_losowania = cut[0]
        numerki = sorted(numerki_tosort)
        print(numerki)
        rekord_z_data=models.LottoNumbers.objects.filter(draw_date=data_losowania)
        print(rekord_z_data)
        if not rekord_z_data:
            models.LottoNumbers.objects.create(
                draw_date=data_losowania,
                draw_number=num_losowania,
                number_1=numerki[0],
                number_2=numerki[1],
                number_3=numerki[2],
                number_4=numerki[3],
                number_5=numerki[4],
                number_6=numerki[5]
            )
        request=request
        print('------------')
        print(request.is_ajax)
        print()
        ctx = {'numerki': ','.join(numerki),
               'num_losowania': num_losowania,
               'data_losowania': data_losowania,
               'request': request.user
               }
        return render(request, 'appefirst/dbd.html', ctx)

    def post(self, request):
        return render(request, 'appefirst/dbd.html')


class ProductView(LoginRequiredMixin, View):
    def get(self, request, id):
        product = models.Products.objects.get(id=id)
        domain = "http://healthy-now-nature.com/"
        ctx = {"prod": product,
               "domain": domain}
        return render(request, 'appefirst/prod_det.html', ctx)


class DomainsView(LoginRequiredMixin, View):
    def get(self, request):
        domains_distinct = models.Domains.objects.all().distinct('domain_owner')
        domains = models.Domains.objects.all()
        ctx = {"domains": domains,
               "domains_distinct": domains_distinct}
        return render(request, 'appefirst/domains.html', ctx)
