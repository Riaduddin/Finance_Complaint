from finance_complaint.constant import TIMESTAMP
import logging
import os
import shutil

LOG_DIR='logs'

def get_log_file_name():
    return f'log_{TIMESTAMP}_file'

LOG_FILE_NAME=get_log_file_name()

if os.path.exist(LOG_DIR):
    shutil.rmtree(LOG_DIR)
os.makedirs(LOG_DIR,exist_ok=True)

LOG_FILE_PATH=os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(filename=LOG_FILE_PATH,
                    filemode='w',
                    format='[%(asctime)s] \t%(levelname)s \t%(lineno)d \t%(filename)s \t%(funcName)s() \t%(message)s',
                    level=logging.INFO
                    )

logger=logging.getLogger('FinanaceComplaint')