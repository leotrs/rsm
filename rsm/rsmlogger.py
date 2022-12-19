# Modified from https://stackoverflow.com/a/56944256/14157230
import logging


class RSMFormatter(logging.Formatter):
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


# Shorten level names for nicer output
logging.addLevelName(logging.DEBUG, "DBG")
logging.addLevelName(logging.INFO, "INF")
logging.addLevelName(logging.WARN, "WRN")
logging.addLevelName(logging.ERROR, "ERROR")
logging.addLevelName(logging.CRITICAL, "CRITICAL")

logger = logging.getLogger("RSM")
logger.setLevel(logging.WARN)
handler = logging.StreamHandler()
handler.setLevel(logging.WARN)
handler.setFormatter(RSMFormatter())
logger.addHandler(handler)
