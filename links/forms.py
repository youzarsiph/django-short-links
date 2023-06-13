""" Forms """


from django import forms
from links.models import URL


class URLForm(forms.ModelForm):
    """ URL Form """
    class Meta:
        """ Meta Data """

        model = URL
        fields = ('url',)
