import logging
import os

# Get the root directory of the project
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Define the logs directory in the root folder
LOG_DIR = os.path.join(ROOT_DIR, 'logs')

# Create the logs directory if it doesn't exist
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Configure logging
LOG_FILE_PATH = os.path.join(LOG_DIR, 'application.log')
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

# Create a logger instance
logger = logging.getLogger('product_logger')
