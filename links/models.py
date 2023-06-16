""" Data Models """


from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


# Create your models here.
class URL(models.Model):
    """ URLs """

    # The owner of shortened url
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text='The owner'
    )
    url = models.URLField(
        unique=True,
        db_index=True,
        help_text='The link to be shortened'
    )
    token = models.CharField(
        max_length=10,
        unique=True,
        db_index=True,
        help_text='Link token'
    )
    clicks = models.BigIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url
