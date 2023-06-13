""" URLConf """


from django.urls import path
from links.views import Index, URLCreateView, URLDetailView, ServeURL


app_name = 'links'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('new/', URLCreateView.as_view(), name='create_url'),
    path('<slug:slug>/', ServeURL.as_view(), name='redirect'),
    path('<int:id>/result/', URLDetailView.as_view(), name='url_detail'),
]
