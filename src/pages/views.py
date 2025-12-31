import os
import platform

from django import get_version
from django.conf import settings
from django.shortcuts import render


def home(request):
    # Use getenv with a sensible fallback so CI and different runtimes work
    python_ver = os.getenv("PYTHON_VERSION") or platform.python_version()

    context = {
        "debug": settings.DEBUG,
        "django_ver": get_version(),
        "python_ver": python_ver,
    }

    return render(request, "pages/home.html", context)
