# url_cutter

URL shortener

url_cutter is a url shortening web application written in python and django.

# Getting Started

First start a project:

```shell
django-admin startproject mysite
cd mysite
```

Clone the repo:

```shell
git clone https://github.com/youzarsiph/url_cutter.git
```

Run the migrations:

```shell
python manage.py migrate
```

Run the server:

```shell
python manage.py runserver
```

Change the site_name, in `url_cutter/views.py`:

```python
...


class URLDetailView(DetailView):
    model = URL
    pk_url_kwarg = 'id'
    template_name = 'url_cutter/detail.html'
    extra_context = {
        # This site_name is for example
        # CHANGE this line, replace it with your domain
        'site_name': 'https://youzarsiph.pythonanywhere.com/url_cutter/'
        # 'site_name': 'https://your.domain.com/'
    }


...
```

I hope that you find this useful.
