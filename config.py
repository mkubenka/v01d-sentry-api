DEBUG = False
SENTRY_DSN = ''

try:
    from local_config import *
except ImportError:
    # No local config found.
    pass