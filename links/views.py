""" Views """


import secrets
from typing import Any

from django.conf import settings
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.forms.forms import BaseForm
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from links.models import URL
from links.mixins import UserFilterMixin


# Create your views here.
class Index(generic.TemplateView):
    """ Index page """

    template_name = 'links/index.html'


class URLCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    """ URL CreateView """

    model = URL
    fields = ['url']
    template_name = "links/create.html"
    success_url = reverse_lazy('links:url_list')
    success_message = 'Link was created successfully'

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        """ Redirect to details or create new instance """

        try:
            url = URL.objects.get(url=request.POST['url'])
            return redirect(reverse_lazy('links:url_detail', args=[url.pk]))

        except URL.DoesNotExist:
            return super().post(request, *args, **kwargs)

    def form_valid(self, form: BaseForm) -> HttpResponse:
        """ Compute the shortened url """

        # Create a url object
        instance: URL = form.save(commit=False)

        # Set the owner and url token
        instance.user = self.request.user
        instance.token = secrets.token_urlsafe(7)

        # Save the object
        instance.save()
        return super().form_valid(form)


class URLListView(LoginRequiredMixin, UserFilterMixin, generic.ListView):
    """ URL List view """

    model = URL
    template_name = 'links/list.html'
    extra_context = {'site_url': settings.LINKS_SITE_URL}


class URLDetailView(LoginRequiredMixin, UserFilterMixin, generic.DetailView):
    """ URL Details """

    model = URL
    pk_url_kwarg = 'id'
    template_name = 'links/detail.html'
    extra_context = {'site_url': settings.LINKS_SITE_URL}


class URLUpdateView(LoginRequiredMixin, UserFilterMixin, SuccessMessageMixin, generic.UpdateView):
    """ URL Update View """

    model = URL
    pk_url_kwarg = 'id'
    fields = ['token', 'url']
    template_name = 'links/update.html'
    success_url = reverse_lazy('links:url_list')
    success_message = 'Link was updated successfully'


class URLDeleteView(LoginRequiredMixin, UserFilterMixin, SuccessMessageMixin, generic.DeleteView):
    """ URL Delete View """

    model = URL
    pk_url_kwarg = 'id'
    template_name = 'links/delete.html'
    success_url = reverse_lazy('links:url_list')
    success_message = 'Link was deleted successfully'


class ServeURL(generic.DetailView):
    """ Redirect URLs """

    model = URL
    slug_field = 'token'

    def get(self, request, *args, **kwargs):
        """ Redirect urls """

        instance = self.get_object()
        instance.clicks += 1
        instance.save()

        return redirect(instance.url)
