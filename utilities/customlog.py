import logging
import inspect


def custom_logger(loglevel=logging.DEBUG):
    logFileName = inspect.stack()[1][3]

    logger = logging.getLogger(logFileName)
    logger.setLevel(loglevel)

    filehandler = logging.FileHandler(filename = "autotest.log")
    filehandler.setLevel(loglevel)


    formatter = logging.Formatter(format('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
                                  datefmt='%m:%d:%Y %I:%M:%S %p')

    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)

    return logger
