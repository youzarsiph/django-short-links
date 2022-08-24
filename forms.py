from django import forms
from url_cutter.models import URL


class URLForm(forms.ModelForm):
    class Meta:
        model = URL
        fields = ('url',)
