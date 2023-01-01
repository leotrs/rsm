"""Configure the logging module for RSM apps."""
import logging

# Official documentation recommends that library code does not setup logging - it is the
# responsibility of client application code.
# https://docs.python.org/3/howto/logging-cookbook.html#adding-handlers-other-than-nullhandler-to-a-logger-in-a-library
logger = logging.getLogger("RSM")
logger.addHandler(logging.NullHandler())


# The rest of this module defines classes and functions that are meant to be used by
# client application code.
class RSMFormatter(logging.Formatter):
    """Default logging formatter for RSM apps."""

    grey = "\x1b[37;2m"
    blue = "\x1b[34;1m"
    white = "\x1b[37;10m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    boldred = "\x1b[31;1m"
    reset = "\x1b[0m"
    prefix = grey + "%(asctime)s " + reset + blue + "%(name)s " + reset
    msgformat = "%(levelname)-3s | %(message)s"
    suffix = reset + grey + " (%(filename)s:%(lineno)d)" + reset

    COLORS = {
        logging.DEBUG: grey,
        logging.INFO: white,
        logging.WARN: yellow,
        logging.ERROR: red,
        logging.CRITICAL: boldred,
    }

    def format(self, record: logging.LogRecord) -> str:
        fmt = (
            self.prefix
            + self.COLORS.get(record.levelno, self.grey)
            + self.msgformat
            + self.suffix
        )
        formatter = logging.Formatter(fmt, datefmt="%H:%M:%S")
        return formatter.format(record)


def config_rsm_logger(verbosity: int = 0):
    """Configure logging for RSM applications.

    By default, the RSM libray creates a logger instance with name "RSM" but it does not
    add any handlers or formatters to it.  Instead, it is the responsibility of client
    application code to setup logging.  This function configures the "RSM" logger in the
    way recommended by library author.  In particular, scripts such as rsm-make and
    rsm-lint use this configuration.

    """
    logger = logging.getLogger("RSM")

    # Shorten level names for nicer output
    logging.addLevelName(logging.DEBUG, "DBG")
    logging.addLevelName(logging.INFO, "INF")
    logging.addLevelName(logging.WARN, "WRN")
    logging.addLevelName(logging.ERROR, "ERROR")
    logging.addLevelName(logging.CRITICAL, "CRITICAL")

    # Setup default handlers
    handler = logging.StreamHandler()
    handler.setLevel(logging.WARN)
    handler.setFormatter(RSMFormatter())
    logger.addHandler(handler)

    # Set level
    level = logging.WARNING - verbosity * 10
    level = max(level, logging.DEBUG)
    logger.setLevel(level)
    for h in logger.handlers:
        if h.level > level:
            h.setLevel(level)
