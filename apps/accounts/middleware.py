from django.utils import timezone

from .models import User


class LastActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        user = getattr(request, "user", None)
        if user is None or not getattr(user, "is_authenticated", False):
            return response
        now = timezone.now()
        last = getattr(user, "last_activity_at", None)
        if last is None or (now - last).total_seconds() > 60:
            User.objects.filter(pk=user.pk).update(last_activity_at=now)
        return response
