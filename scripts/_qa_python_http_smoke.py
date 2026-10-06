"""HTTP smoke: Python lecture page + run endpoint."""
from __future__ import annotations

import json
import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import django

django.setup()

from django.contrib.auth import get_user_model
from django.test import Client
from django.urls import reverse

from apps.courses.models import Lecture


def main() -> int:
    User = get_user_model()
    admin = User.objects.filter(is_superuser=True).first()
    client = Client()
    client.force_login(admin)

    lec = Lecture.objects.get(slug="py-noldan-start")
    url = reverse("learning:lecture", args=[lec.pk])
    run = reverse("learning:run_python", args=[lec.pk])
    print("url", url)
    print("run", run)

    r = client.get(url)
    body = r.content.decode("utf-8", "replace")
    print("lecture_status", r.status_code)
    for marker in (
        "python-playground",
        "py-run-form",
        "Oddiy tilda",
        "py-editor",
        "py-visual",
    ):
        print(marker, marker in body)

    r2 = client.post(
        run,
        data=json.dumps({"code": "print(2+2)"}),
        content_type="application/json",
    )
    print("run_json", r2.status_code, r2.content[:300])

    r3 = client.post(run, {"code": "print('hi')"})
    print("run_form", r3.status_code, r3.content[:300])

    free = User.objects.filter(is_superuser=False, is_staff=False).first()
    print("free_user", free)
    if free:
        c2 = Client()
        c2.force_login(free)
        r4 = c2.get(url)
        print(
            "free_start",
            r4.status_code,
            "playground",
            b"python-playground" in r4.content,
        )
        later = Lecture.objects.get(slug="pd-df")
        r5 = c2.get(reverse("learning:lecture", args=[later.pk]))
        print("free_later", r5.status_code, "locked_hint", b"premium" in r5.content.lower() or b"Premium" in r5.content or r5.status_code in (302, 403))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
