import logging
import os
from datetime import datetime

# Generate a unique log file name using the current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the directory for log files
log_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Create the log directory if it doesn't already exist
os.makedirs(log_path, exist_ok=True)

# Define the full path to the log file
LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
