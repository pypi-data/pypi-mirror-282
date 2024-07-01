import logging
from django.http import HttpResponseForbidden
from django.conf import settings
from django.urls import reverse

logger = logging.getLogger(__name__)


class IPRestrictionMiddleware:
    """
    Middleware for restricting access based on IP addresses.

    This middleware checks if the client's IP address is allowed to access certain URL paths.
    It reads the allowed IP addresses from Django settings and enforces access restrictions.

    Args:
        get_response (callable): The next middleware or view function in the chain.

    Attributes:
        allowed_ips (set): Set of allowed IP addresses.
        allowed_admin_ips (set): Set of allowed IP addresses for admin paths.
        url (str): URL path for the admin interface.
    """
    def __init__(self, get_response):
        self.get_response = get_response
        self.allowed_ips = set(settings.ALLOWED_IPS)
        self.allowed_admin_ips = set(settings.ALLOWED_ADMIN_IPS)
        self.restricted_paths_and_IP = self.parse_restricted_paths(settings.RESTRICTED_PATH)
        self.url = self.get_admin_url()

    def __call__(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        remote_ip = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')

        if request.path.startswith(self.url):
            if '*' not in self.allowed_admin_ips and remote_ip not in self.allowed_admin_ips:
                self.log_restricted_ip(remote_ip, request.path)
                return HttpResponseForbidden("Access Denied")   
        elif request.path in self.restricted_paths_and_IP:
            if '*' not in self.allowed_ips and remote_ip not in self.allowed_ips:
                self.log_restricted_ip(remote_ip, request.path)
                return HttpResponseForbidden("Access Denied")
        
        for path, allowed_ips in self.restricted_paths_and_IP.items():
            if path in request.path:
                if '*' not in allowed_ips and remote_ip not in allowed_ips:
                    self.log_restricted_ip(remote_ip, request.path)
                    return HttpResponseForbidden("Access Denied")
                break
            
        if '*' not in self.allowed_ips and remote_ip not in self.allowed_ips:
            self.log_restricted_ip(remote_ip, request.path)
            return HttpResponseForbidden("Access Denied")

        return self.get_response(request)
    
    def parse_restricted_paths(self, restricted_paths):
        parsed_paths = {}
        for ips, paths in restricted_paths.items():
            ip_list = [ip.strip() for ip in ips.split(',')]
            for path in paths:
                if path not in parsed_paths:
                    parsed_paths[path] = set()
                parsed_paths[path].update(ip_list)
        return parsed_paths
    
    def get_admin_url(self):
        """
        Get the admin URL path. Defaults to Django admin URL if not set.
        """
        default_admin_url = reverse('admin:index')
        force_script_name = settings.FORCE_SCRIPT_NAME or ''
        return force_script_name + default_admin_url

    def log_restricted_ip(self, ip, path):
        """
        Log the restricted IP access attempt.

        Args:
            ip (str): The IP address of the client.
            path (str): The requested URL path.
        """
        logger.warning(f"Access denied for IP: {ip} on path: {path}")
