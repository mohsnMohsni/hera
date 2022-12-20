from .models import IPAddress


class SaveIPAddressMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for
        else:
            ip = request.META.get('REMOTE_ADDR')
        try:
            ip_address = IPAddress.objects.get(ip_address=ip)
        except IPAddress.DoesNotExist:
            ip_address = IPAddress.objects.create(ip_address=ip)
        request.user.ip_address = ip_address
        response = self.get_response(request)
        return response
