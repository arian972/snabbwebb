#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.core.management.utils import get_random_secret_key
from django.apps import AppConfig
import os

def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "snabbwebb.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
