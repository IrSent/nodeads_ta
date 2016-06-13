from time import time
from logging import getLogger

class CustomLoggingMiddleware(object):
    def __init__(self):
        self.logger = getLogger('django.request')

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
          ip = request.META.get('REMOTE_ADDR')
        return ip

    def process_response(self, request, response):
        self.logger.info(
            '[%s] %s %s',
            response.status_code,
            request.get_full_path(),
            self.get_client_ip(request)
        )
        return response