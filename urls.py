from django.urls import path
from url_cutter.views import Index


urlpatterns = [
    path('', Index.as_view(), name='index'),
]
