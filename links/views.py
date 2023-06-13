""" Views """


import secrets

from django.conf import settings
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView, DetailView

from links.forms import URLForm
from links.models import URL


# Create your views here.
class Index(TemplateView):
    """ Index page """

    template_name = 'links/index.html'
    extra_context = {'form': URLForm()}


class URLCreateView(CreateView):
    """ URL CreateView """

    model = URL
    form_class = URLForm
    template_name = "links/index.html"
    success_url = reverse_lazy('links:index')

    def post(self, request, *args, **kwargs):
        """ Redirect to details or create new instance """

        try:
            url = URL.objects.get(url=request.POST['url'])
            return redirect(reverse_lazy('links:url_detail', args=[url.id]))

        except URL.DoesNotExist:
            return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        """ Compute the shortened url """

        # Create a url object
        instance = form.save(commit=False)

        # Set url token
        instance.token = secrets.token_urlsafe(7)

        # Save the object
        instance.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy('links:url_detail', args=[self.object.id])


class URLDetailView(DetailView):
    """ URL Details """

    model = URL
    pk_url_kwarg = 'id'
    template_name = 'links/detail.html'
    extra_context = {'site_url': settings.LINKS_SITE_URL}


class ServeURL(DetailView):
    """ Redirect URLs """

    model = URL
    slug_field = 'token'

    def get(self, request, *args, **kwargs):
        """ Redirect urls """

        instance = self.get_object()
        instance.clicks += 1
        instance.save()

        return redirect(instance.url)
