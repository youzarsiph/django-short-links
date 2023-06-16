""" URLConf """


from django.urls import path
from links import views


app_name = 'links'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('links/', views.URLListView.as_view(), name='url_list'),
    path('links/new/', views.URLCreateView.as_view(), name='create_url'),
    path('links/<int:id>/', views.URLDetailView.as_view(), name='url_detail'),
    path('links/<int:id>/update/', views.URLUpdateView.as_view(), name='update_url'),
    path('links/<int:id>/delete/', views.URLDeleteView.as_view(), name='delete_url'),
    path('<slug:slug>/', views.ServeURL.as_view(), name='redirect'),
]
