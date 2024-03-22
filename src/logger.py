import logging
'''
It is sued to log the exceptions means it helps to track the errors we are getting..
'''
import os
from datetime import datetime
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE) # getcwd --> current working directory
os.makedirs(logs_path,exist_ok=True) # It will appends the file as we creat the files..

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format = '[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level= logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging has started")