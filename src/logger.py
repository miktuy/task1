import logging
import sys


logger = logging.getLogger(__name__)
h = logging.StreamHandler(sys.stdout)
h.flush = sys.stdout.flush
h.setFormatter(logging.Formatter(fmt="""--------------------------------------------------------------------
{levelname} - {asctime} - {message}
--------------------------------------------------------------------""", style="{"))
logger.addHandler(h)
logger.setLevel("INFO")
