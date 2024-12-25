import logging

def logger():
    log = logging.getLogger("Login Test")
    log.setLevel(logging.DEBUG)
    handler = logging.FileHandler("test_execution.log")
    handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    log.addHandler(handler)
    return log