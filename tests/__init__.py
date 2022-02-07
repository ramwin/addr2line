import logging


stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler("info.log", mode="a")

logging.basicConfig(
    level=logging.INFO,
    format=(
        '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
    ),
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        stream_handler,
        file_handler,
    ],
)
