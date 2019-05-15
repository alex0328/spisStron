from django.shortcuts import render
from django.views import View
from appefirst import models


class MainPageView(View):
    def get(self, request):
        return render(request, 'appefirst/index.html')