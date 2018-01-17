from django.views.generic import View

from rest_framework.settings import api_settings
from  .pagination import PageNumberPagination


class GenericPaginationClass(View):
    # def __init__(self, pagination_class):
    #     super(GenericPaginationClass, self).__init__()
    #     self.pagination_class = pagination_class

    @property
    def paginator(self):
        """
        The paginator instance associated with the view, or `None`.
        """
        # self.pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
        self.pagination_class = PageNumberPagination

        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        return self._paginator

    def paginate_queryset(self, queryset):
        """
        Return a single page of results, or `None` if pagination is disabled.
        """
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
        """
        Return a paginated style `Response` object for the given output data.
        """
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)
