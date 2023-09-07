#!/usr/bin/env python
import os
import sys

from dotenv import load_dotenv
from decouple import config

load_dotenv()
# if __name__ == "__main__":
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jgdesigns.settings.dev")
#     # os.environ.setdefault("DJANGO_SETTINGS_MODULE", os.getenv("DJANGO_SETTINGS_MODULE", "jgdesigns.settings.production"))

#     from django.core.management import execute_from_command_line

#     execute_from_command_line(sys.argv)

if __name__ == "__main__":
    if "DJANGO_SETTINGS_MODULE" not in os.environ:
        # If DJANGO_SETTINGS_MODULE is not set, assume production
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jgdesigns.settings.production")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", os.getenv("DJANGO_SETTINGS_MODULE"))

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)