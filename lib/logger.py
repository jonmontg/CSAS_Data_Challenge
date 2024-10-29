import logging
from pathlib import Path

log_file = str(Path("logs") / "logs.txt")
logger = logging.getLogger("csas_data_challenge_logger")
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler(log_file, mode="w")
fh.setLevel(logging.DEBUG)
fh.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
logger.addHandler(fh)
