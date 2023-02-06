""" Forms """


from django import forms
from url_cutter.models import URL


class URLForm(forms.ModelForm):
    """ URL Form """
    class Meta:
        """ Meta Data """

        model = URL
        fields = ('url',)
