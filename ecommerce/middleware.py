import re
from django.conf import settings
from django.shortcuts import redirect
from django.utils.http import url_has_allowed_host_and_scheme
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect
from django.urls import reverse

EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings,'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]


class LoginRequiredMiddleware(MiddlewareMixin):
    def __init__(self,get_response):
        # print(get_response)
        # pass
        self.get_response = get_response

    def __call__(self,request):
        # Here I call login if not authenticated and request is not login page
        if not request.user.is_authenticated and request.path != reverse('index'):
            return HttpResponseRedirect(reverse('index'))  
        response = self.get_response(request)
        return response
    