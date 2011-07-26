#!/usr/bin/env python2

from django.core.management import execute_manager

try:
    import local_settings as settings
except ImportError:
    import sys
    
    sys.stderr.write("Error: Can't find the file 'local_settings.py' in the "
        "directory containing '%s'.\nIf your settings file is named something "
        "else please specify it using --settings parameter.\n" % __file__)
    sys.exit(1)

if __name__ == "__main__":
    execute_manager(settings)