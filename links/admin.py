""" Admin Site Model Registration """


from django.contrib import admin
from links.models import URL


# Register your models here.
admin.site.register(URL)
