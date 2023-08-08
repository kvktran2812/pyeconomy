import logging


class CustomFormatter(logging.Formatter):
    grey = "\x1b[37m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


# TODO: update better logging to file
class ModelLogger(logging.Logger):
    def __init__(self, name: str, log_to_file: bool = False):
        super().__init__(name)
        self.setLevel(logging.DEBUG)

        # create StreamHandler
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)
        formatter = CustomFormatter()
        stream_handler.setFormatter(formatter)
        self.addHandler(stream_handler)

        if log_to_file:
            # create FileHandler
            file_handler = logging.FileHandler(f"{name}.log")
            file_handler.setLevel(logging.ERROR)
            formatter = logging.Formatter()
            file_handler.setFormatter(formatter)
            self.addHandler(file_handler)

