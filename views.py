""" Views """


import secrets

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView, CreateView, DetailView

from url_cutter.forms import URLForm
from url_cutter.models import URL


# Create your views here.
class Index(TemplateView):
    """ Index page """

    template_name = 'url_cutter/index.html'
    extra_context = {
        'form': URLForm()
    }


class URLCreateView(CreateView):
    """ URL CreateView """

    model = URL
    form_class = URLForm
    template_name = "url_cutter/index.html"
    success_url = reverse_lazy('url_cutter:index')

    def post(self, request, *args, **kwargs):
        """ Redirect to details or create new instance """

        try:
            url = URL.objects.get(url=request.POST['url'])
            return redirect(reverse_lazy('url_cutter:url_detail', args=[url.id]))

        except ObjectDoesNotExist:
            return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        """ Compute the shortened url """

        # Save without committing
        instance = form.save(commit=False)

        # Set user and url token
        instance.user = self.request.user
        instance.shortened = secrets.token_urlsafe(7)

        # Save the object
        instance.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy('url_cutter:url_detail', args=[self.object.id])


class URLDetailView(DetailView):
    """ URL Details """

    model = URL
    pk_url_kwarg = 'id'
    template_name = 'url_cutter/detail.html'
    extra_context = {
        # This site_name is for example
        'site_name': 'https://youzarsiph.pythonanywhere.com/url_cutter/'
        # 'site_name': 'https://your.domain.com/url_cutter/'
    }


class ServeURL(DetailView):
    """ Redirect URLs """

    model = URL
    slug_field = 'shortened'

    def get(self, request, *args, **kwargs):
        """ Redirect urls """

        instance = self.get_object()
        instance.clicks = instance.clicks + 1
        instance.save()
        return redirect(instance.url)
