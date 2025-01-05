from src.mlproject.logger import logging
from src.mlproject.exception_handing import customException
import sys

if __name__=="__main__":
    logging.info("the excution is started")

    try:
        a=1/0
    except Exception as e:
        logging.info("custom exception")
        raise customException(e,sys)