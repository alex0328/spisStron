from django.urls import path
from appefirst import views
from django.conf.urls.static import static
from django.conf import settings



app_name = 'appefirst'
urlpatterns = [
    path('', views.MainPageView.as_view(), name='index'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)