from functools import wraps
from django.http import HttpResponseForbidden

def admin_required(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == 'admin':
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You are not authorized to access this page.")
    return wrapped_view


def manager_required(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role in ['admin', 'manager']:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You are not authorized to access this page.")
    return wrapped_view


def user_required(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You are not authorized to access this page.")
    return wrapped_view

