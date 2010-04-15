from django.conf import settings
from django.http import HttpResponse

# Merge with original namespace so user
# doesn't have to import twice.
from django.shortcuts import *


__all__ = ('render_to_string', 'render_to_response',)


# Is within ``template.loader`` as per Django specification -
# but I think it fits very well here.
from coffin.template.loader import render_to_string


def render_to_response(template_name, context=None, context_instance=None,
                       mimetype=None, status=200, content_type=None):
    """
    :param template_name: Filename of the template to get or a sequence of
        filenames to try, in order.
    :param context: Rendering context for the template.
    :returns: A response object with the evaluated template as a payload.
    """
    if content_type is None:
        content_type = getattr(settings, 'DEFAULT_CONTENT_TYPE', 'text/html')
    content = render_to_string(template_name, context, context_instance)
    return HttpResponse(content, mimetype=mimetype, status=status,
        content_type=content_type)
