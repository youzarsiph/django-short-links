""" Mixins """


from typing import Any
from django.db.models.query import QuerySet


# Create your mixins here.
class UserFilterMixin:
    """ Filter the queryset by user """

    def get_queryset(self) -> QuerySet[Any]:
        """ Filter queryset by user """

        return super().get_queryset().filter(user=self.request.user)
