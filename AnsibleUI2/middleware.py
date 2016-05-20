#!/usr/bin/env python
import logging

import django.views.static
import django.views.generic.base
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.http import urlquote

from django.contrib.auth import REDIRECT_FIELD_NAME

LOG = logging.getLogger(__name__)
MIDDLE_WARE_HEADER = "X-Middleware-Response"

# Views inside Django that don't require login
# (see LoginAndPermissionMiddleware)
DJANGO_VIEW_AUTH_WHITE_LIST = [
  django.views.static.serve,
  django.views.generic.base.RedirectView,
]


class AjaxMiddleware(object):
    """
    Middleware that augments request to set request.ajax
    for either is_ajax() (looks at HTTP headers) or ?format=json
    GET parameters.
    """

    def process_request(self, request):
        request.ajax = request.is_ajax() or \
            request.GET.get("format", "") == "json"
        return None


class LoginAndPermissionMiddleware(object):
    """
    Middleware that forces all views (except those that opt out)
    through authentication.
    """

    def process_view(self, request, view_func, view_args, view_kwargs):
        # If the view has "opted out" of login required, skip
        if hasattr(view_func, "login_not_required"):
            return None

        # There are certain django views which are also opt-out, but
        # it would be evil to go add attributes to them
        if view_func in DJANGO_VIEW_AUTH_WHITE_LIST:
            return None

        if request.user.is_active and request.user.is_authenticated():
            return None

        # Send back a magic header which causes Hue.Request to interpose itself
        # in the ajax request and make the user login before resubmitting the
        # request.
        if request.ajax:
            response = HttpResponse("/* login required */",
                                    content_type="text/javascript")
            response[MIDDLE_WARE_HEADER] = 'LOGIN_REQUIRED'
            return response
        else:
            return HttpResponseRedirect("%s?%s=%s" % (settings.LOGIN_URL,
                            REDIRECT_FIELD_NAME,
                            urlquote(request.get_full_path())))
