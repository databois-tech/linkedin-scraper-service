import logging
import coloredlogs

# Configure the logger
coloredlogs.install(
    level='DEBUG',  # Set the desired log level
    fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

# Create a logger
logger = logging.getLogger('Dotty-tech')