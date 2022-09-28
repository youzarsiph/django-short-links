from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class URL(models.Model):
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
    )
    clicks = models.BigIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
