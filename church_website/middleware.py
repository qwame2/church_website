class CDNNoCacheMiddleware:
    """
    Middleware that explicitly instructs CDNs not to cache any response that contains a Set-Cookie header.
    This prevents Session or CSRF token leakage across multiple edge connections.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # If any cookie is being set (usually sessionid or csrftoken or messages), explicitly stop caches
        if response.has_header('Set-Cookie'):
            # Override caching headers explicitly
            response['Cache-Control'] = 'private, no-cache, no-store, must-revalidate, max-age=0'
            response['Pragma'] = 'no-cache'
            response['Expires'] = '0'
            
        return response
