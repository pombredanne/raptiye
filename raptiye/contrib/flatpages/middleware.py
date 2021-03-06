# coding: utf-8

from django.conf import settings
from django.http import Http404

from views import flatpage


__all__ = (
    'FlatpageFallbackMiddleware',
)


class FlatpageFallbackMiddleware(object):
    def process_response(self, request, response):
        if response.status_code != 404:
            return response  # No need to check for a flatpage for non-404 responses.

        try:
            return flatpage(request, request.path_info)
        except Http404:
            # Return the original response if any errors happened. Because this
            # is a middleware, we can't assume the errors will be caught elsewhere.
            return response
        except:
            if settings.DEBUG:
                raise

            return response
