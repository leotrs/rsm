# Modified from https://stackoverflow.com/a/56944256/14157230
import logging


class CustomFormatter(logging.Formatter):
    grey = "\x1b[37;2m"
    blue = "\x1b[34;1m"
    white = "\x1b[37;10m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    boldred = "\x1b[31;1m"
    reset = "\x1b[0m"
    prefix = grey + '%(asctime)s ' + reset + blue + '%(name)s ' + reset
    msgformat = "%(levelname)-7s | %(message)s"
    suffix =  reset + grey + " (%(filename)s:%(lineno)d)" + reset

    COLORS = {
        logging.DEBUG: grey,
        logging.INFO: white,
        logging.WARNING: yellow,
        logging.ERROR: red,
        logging.CRITICAL: boldred,
    }

    def format(self, record):
        fmt = self.prefix + self.COLORS[record.levelno] + self.msgformat + self.suffix
        formatter = logging.Formatter(fmt, datefmt='%H:%M:%S')
        return formatter.format(record)


logger = logging.getLogger('RSM')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
handler.setFormatter(CustomFormatter())
logger.addHandler(handler)
