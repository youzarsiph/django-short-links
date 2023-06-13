""" Data Models """


from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


# Create your models here.
class URL(models.Model):
    """ URLs """

    url = models.URLField(
        unique=True,
        db_index=True,
        help_text='The URL to be shortened'
    )
    token = models.CharField(
        max_length=10,
        unique=True,
        db_index=True
    )
    clicks = models.BigIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url
