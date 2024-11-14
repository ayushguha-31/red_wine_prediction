import sys
import os

# Add the 'src' directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

# Now you can import your modules
from mlProject import logger

# Your main code logic goes here
if __name__ == "__main__":
    # Example of logging
    logger.info("This is a test log message from the main script.")
