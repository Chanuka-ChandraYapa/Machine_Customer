import logging
import os

# Create a logs directory if it doesn't exist
if not os.path.exists('logs'):
    print("create")
    os.makedirs('logs')

# Configure logging
logging.basicConfig(
    filename='logs/application.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

# Create a logger instance
logger = logging.getLogger('product_logger')

logger.setLevel(logging.INFO)

# Create a file handler for saving logs to a file
file_handler = logging.FileHandler("app.log")  # Logs will be saved to app.log
file_handler.setLevel(logging.INFO)

# Set log format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

# Remove default handlers (if any)
logger.propagate = False

