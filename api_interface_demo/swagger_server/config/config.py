import os
import pathlib
import logging

# Path to config file
PATH_CONFIG = pathlib.Path(__file__).resolve().parent

# Path to the app
APP_ROOT = pathlib.Path(PATH_CONFIG).resolve().parent

# Logging file
LOG_FILE = APP_ROOT / 'log_file.log'

# sensor types
SENSOR_TYPES = ['SENSOR_NODE', 'ASSET_SENSOR']

# models (if the AWS sitewise models are modified, the MODELS and HIERARCHY_MODELS IDs need to be set again here)
MODELS = {
    'SITE_MODEL': '14c668fe-0b85-428a-ba5c-1468e0b283d6',
    'ZONE_MODEL': '83ce422b-d401-4655-a7b2-794f19e93176',
    'SENSOR_NODE_MODEL': '561b2085-8de9-44fb-922a-ebacc78adf1b',
    'ASSET_SENSOR_MODEL': '292322a8-3118-4ce1-b9e5-adb1b91c58cb'
}

# hierarchies
HIERARCHY_MODELS = {
    'SENSOR_NODE': 'be8d41f7-6c88-4ea5-9df9-c5c4f9b22e0d',
    'ASSET_SENSOR': '2356270a-66c5-49ee-a849-5288ccc86bb4',
    'ZONE': 'ee388cad-61fd-449a-ad6d-b09c6a35aa99'}

# old
# # models
# MODELS = {
#     'SITE_MODEL': '17047748-3af7-4216-8d85-516b9bf975d5',
#     'ZONE_MODEL': '7a550ef3-ada5-40af-b724-26015d6b4a1b',
#     'SENSOR_NODE_MODEL': '1d73d32b-0cde-4c82-99cb-6755a3148ec2',
#     'ASSET_SENSOR_MODEL': '8b483611-6392-4a7f-9261-89a16fb8cef6'
# }
#
# # hierarchies
# HIERARCHY_MODELS = {
#     'SENSOR_NODE': '4298ea66-a591-4fed-90c6-f7b97e4af239',
#     'ASSET_SENSOR': '1611f062-2b3b-4d5b-a4b1-37ad9526823b',
#     'ZONE': '1df6e4ae-7836-4efd-891d-80a0d74de1e2'}


WAIT_TIME = 30  # seconds
WAIT_INTERVAL = 4  # seconds

PROPERTIES_WITH_ALIAS = ['Temperature', 'Movement', 'Humidity']


# Logger
FORMAT_MAIN_LOGGER = logging.Formatter(
    "%(asctime)s — %(name)s — %(levelname)s —"
    "%(funcName)s:%(lineno)d — %(message)s")

LOGGER_LEVEL_CONSOLE = 'DEBUG'
LOGGER_LEVEL_FILE = 'INFO'


# Security  # TODO
SECRET_KEY = "SecretKey"


def config_logger(logger):

    # Config level
    logging.basicConfig(
        level=logging.DEBUG)  # To log everything, by default it only logs warning and above.

    # Create handlers
    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler(LOG_FILE)

    # set levels
    if hasattr(logging, LOGGER_LEVEL_CONSOLE):
        c_handler.setLevel(getattr(logging, LOGGER_LEVEL_CONSOLE))
    if hasattr(logging, LOGGER_LEVEL_FILE):
        f_handler.setLevel(getattr(logging, LOGGER_LEVEL_FILE))

    # Create formatters and add it to handlers
    c_handler.setFormatter(FORMAT_MAIN_LOGGER)
    f_handler.setFormatter(FORMAT_MAIN_LOGGER)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    logger.propagate = False

    return logger


