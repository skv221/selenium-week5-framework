import logging

def logger(reportDir):
    log = logging.getLogger("Login Test")
    log.setLevel(logging.DEBUG)
    handler = logging.FileHandler(reportDir)
    handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    log.addHandler(handler)
    return log