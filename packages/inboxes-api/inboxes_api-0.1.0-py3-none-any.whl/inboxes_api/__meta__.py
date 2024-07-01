import sys

__package__ = "inboxes_api"
__version__ = "0.0.1"

SERVER_SOFTWARE: str = "Python/{0[0]}.{0[1]} {1}/{2}".format(
    sys.version_info, __package__, __version__
)
