import logging


class ModelLogger(logging.Logger):
    def __init__(self, name: str, include_time: bool = False):
        super().__init__(name)
        self.include_time = include_time
        self.setLevel(logging.DEBUG)

        # create StreamHandler
        self.stream = logging.StreamHandler()
        self.stream.setLevel(logging.DEBUG)
        formatter = None
        if self.include_time:
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        else:
            formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        self.stream.setFormatter(formatter)
        self.addHandler(self.stream)
