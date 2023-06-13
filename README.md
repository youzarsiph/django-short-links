# django-short-links

URL / Link shortener web app.

## Getting Started

Install `links`:

```shell
pip install django-short-links
```

Add `links` to `INSTALLED_APPS` and add a new setting `LINKS_SITE_NAME`, in `settings.py`:

```python
# settings.py

INSTALLED_APPS = [
    ...
    'links',
    ...
]

# Your server's IP address without trailing slash
LINKS_SITE_URL = 'https://your.domain.com'
```

Include `links` URLConf, in project's `urls.py`:

```python
# urls.py

urlpatterns = [
    ...
    path('l/', include('links.urls')),
    ...
]
```

Run `migrate`:

```shell
python manage.py migrate
```

Now, you can open your browser at `https://your.domain.com/l/`.

I hope that you find this useful.
