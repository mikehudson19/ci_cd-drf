from django.shortcuts import redirect


class RoleBasedAccessControlMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Skip middleware for staff and superusers
        print('user', request.user )
        # if request.user.is_authenticated and not request.user.is_staff and not request.user.is_superuser:
        if not request.user.groups.filter(name='Admin').exists():
            # Redirect to a no-permission page if user is not in the Admin group
            if not request.path.startswith('/api'):
                return redirect('/no-permission/')
        response = self.get_response(request)
        return response