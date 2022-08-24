import random
from hashlib import sha512
from url_cutter.models import URL
from url_cutter.forms import URLForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, DetailView


# Create your views here.
class Index(TemplateView):
    template_name = 'url_cutter/index.html'
    extra_context = {
        'form': URLForm()
    }


class URLCreateView(LoginRequiredMixin, CreateView):
    model = URL
    form_class = URLForm
    template_name = "url_cutter/index.html"
    success_url = reverse_lazy('url_cutter:index')

    def post(self, request, *args, **kwargs):
        """
        If the submitted url exists in the database, redirect the user to detail page of the existing object
        else create the URL object.
         """
        try:
            url = URL.objects.get(url=request.POST['url'])
            return redirect(reverse_lazy('url_cutter:url_detail', args=[url.id]))
        except ObjectDoesNotExist:
            return super(URLCreateView, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        """ Compute the shortened url """

        # Save without committing
        instance = form.save(commit=False)
        instance.user = self.request.user

        # String for computing the hash
        hash_string = str(self.request.user.password)
        hash_string += str(self.request.user.get_full_name())
        hash_string += str(instance.url) + str(self.request.user)

        # Compute sha512 hash
        result = str(sha512(hash_string.encode()).hexdigest())
        # print(result)

        # Compute the shortened url id and assign it
        shortened = ''
        for i in range(10):
            letter = result[random.randint(0, len(str(result))) - 1]
            shortened += letter.upper() if random.randint(0, 1) and letter.isalpha() else letter

        instance.shortened = shortened

        # Save the object
        instance.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy('url_cutter:url_detail', args=[self.object.id])


class URLDetailView(DetailView):
    model = URL
    pk_url_kwarg = 'id'
    template_name = 'url_cutter/detail.html'
    extra_context = {
        # This site_name is for example
        'site_name': 'https://urlcutter.com/'
    }


class ServeURL(DetailView):
    model = URL
    slug_field = 'shortened'

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        return redirect(instance.url)
