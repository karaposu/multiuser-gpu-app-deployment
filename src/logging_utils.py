import logging
from datetime import datetime

# Basic configuration of the logging
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def get_logger(name):
    # Configure the logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Create a console handler or file handler
    handler = logging.StreamHandler()

    # Create a formatter and set it for the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    if not logger.handlers:  # Avoid adding handlers multiple times
        logger.addHandler(handler)

    return logger



def log_user_action(user_id: str, action: str, details: str = ""):
    """
    Logs a user action with optional details.

    :param user_id: Unique identifier for the user.
    :param action: The action the user has performed.
    :param details: Optional additional details about the action.
    """
    log_message = f"User ID: {user_id} | Action: {action} | Details: {details}"
    logging.info(log_message)