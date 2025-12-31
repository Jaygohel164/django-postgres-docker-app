import os
import sys
import platform

from django import get_version
from django.conf import settings
from django.shortcuts import render


def home(request):
    # Use environ.get with a sensible fallback (sys.version) so CI and different runtimes work
    # sys.version.split()[0] returns just the version number (e.g., "3.13.11")
    python_ver = os.environ.get("PYTHON_VERSION", sys.version.split()[0])

    context = {
        "debug": settings.DEBUG,
        "django_ver": get_version(),
        "python_ver": python_ver,
    }

    return render(request, "pages/home.html", context)
