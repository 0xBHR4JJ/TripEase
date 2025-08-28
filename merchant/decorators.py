from django.core.exceptions import PermissionDenied

def merchant_required(view_func):
    def _wrapped(request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated or getattr(user, "role", None) != "merchant":
            raise PermissionDenied("Merchant access only.")
        # also ensure a profile exists
        if not hasattr(user, "merchantprofile"):
            raise PermissionDenied("Merchant profile missing.")
        return view_func(request, *args, **kwargs)
    return _wrapped
