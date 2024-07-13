import os
import sys
import logging 

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]" 
# taking ASCII time, save time stamp and give log level 
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir,exist_ok = True)

logging.basicConfig(
    level = logging.INFO,
    format = logging_str,
    handlers = [
        logging.FileHandler(log_filepath),  #create logging info under both filepath and terminal
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("TextSummizationLogger")