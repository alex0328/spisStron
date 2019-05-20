from django.shortcuts import render
from django.views import View
from appefirst import models


class MainPageView(View):
    def get(self, request):
        content = models.Country.objects.all()
        ctx = {"content": content}
        for con in content:
            print (con)
        return render(request, 'appefirst/index.html', ctx)