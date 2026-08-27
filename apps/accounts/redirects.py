from django.utils.http import url_has_allowed_host_and_scheme


def safe_next_url(request, candidate: str | None, fallback: str | None = None) -> str | None:
    """Faqat shu hostga qaytishga ruxsat (open redirect himoyasi)."""
    if not candidate:
        return fallback
    if url_has_allowed_host_and_scheme(
        url=candidate,
        allowed_hosts={request.get_host()},
        require_https=request.is_secure(),
    ):
        return candidate
    return fallback
