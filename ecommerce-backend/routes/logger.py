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
