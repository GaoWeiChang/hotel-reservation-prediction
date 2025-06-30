import logging
import os # work with directory
from datetime import datetime

# create directory
LOGS_DIR = "logs"
os.makedirs(LOGS_DIR, exist_ok=True) # if exist, dont create

# create log file path
LOG_FILE = os.path.join(LOGS_DIR, f"log_{datetime.now().strftime('%Y-%m-%d')}.log") # ex. log_2023-10-01.log

# logging is log the events in the application
# configure logging

'''
    %(asctime)s = วันที่และเวลา
    %(levelname)s = ระดับความสำคัญ (INFO, ERROR, WARNING)
    %(message)s = ข้อความที่เราส่งเข้ามา
'''
logging.basicConfig(
    filename=LOG_FILE, # รูปแบบข้อความ log
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO # ระดับความสำคัญของ log ที่เราต้องการบันทึก (DEBUG, INFO, WARNING, ERROR, CRITICAL,...) in this case INFO upper
)
'''
    ex.
    2024-06-23 14:30:15,123 - INFO - User logged in
    2024-06-23 14:31:20,456 - ERROR - Database connection failed
'''


def get_logger(name):
    logger = logging.getLogger(name) 
    logger.setLevel(logging.INFO) 
    return logger