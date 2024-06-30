import logging

LOGGER = logging.getLogger(name=__name__)
LOGGER.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)

formatter = logging.Formatter(
    fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

handler.setFormatter(fmt=formatter)

LOGGER.addHandler(hdlr=handler)
