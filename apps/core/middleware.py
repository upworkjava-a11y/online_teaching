import logging
import time

logger = logging.getLogger("apps.core")


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        started = time.monotonic()
        response = self.get_response(request)
        elapsed_ms = int((time.monotonic() - started) * 1000)
        if response.status_code >= 400:
            logger.warning(
                "request_error",
                extra={
                    "path": request.path,
                    "method": request.method,
                    "status": response.status_code,
                    "elapsed_ms": elapsed_ms,
                    "user_id": getattr(request.user, "pk", None) if hasattr(request, "user") else None,
                },
            )
        return response
