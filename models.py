""" Data Models """


from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


# Create your models here.
class URL(models.Model):
    """ URLs """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    url = models.URLField(
        unique=True,
        help_text='The URL to be shortened'
    )
    shortened = models.CharField(
        max_length=16,
        unique=True,
        db_index=True
    )
    clicks = models.BigIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url


class Country(models.Model):
    """ Countries """

    name = models.CharField(
        max_length=32,
        unique=True,
        db_index=True
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class City(models.Model):
    """ Cities """

    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=32,
        unique=True,
        db_index=True
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Click(models.Model):
    """ Clicks """

    url = models.ForeignKey(
        URL,
        on_delete=models.CASCADE
    )
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE
    )
