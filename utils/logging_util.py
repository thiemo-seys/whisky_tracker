import logging

# TODO: this name is maybe a bit too long?
logger = logging.getLogger('whisky_tracker.config_logging_level_parser')

''''
input:str =receives an parameter from the json config file

returns:dict =returns a dict with the keys level corresponding to the logging level and status corresponding to if a valid level was given
'''


# TODO: this feels hacky in some ways, maybe working with exceptions that get returned would be better than using the load status int variable
# but it works for now....
def get_logging_level_from_parameter(logging_parameter):
    is_valid = True
    try:
        logger.debug(f'parsing logging parameter: {logging_parameter.upper()}')
        logging_parameter = logging_parameter.upper()
        if logging_parameter == "DEBUG":
            logging_level = logging.DEBUG
        elif logging_parameter == 'INFO':
            logging_level = logging.INFO
        elif logging_parameter == 'WARNING':
            logging_level = logging.WARNING
        elif logging_parameter == 'ERROR':
            logging_level = logging.ERROR
        elif logging_parameter == 'CRITICAL':
            logging_level = logging.CRITICAL
        else:
            logging.warning(f'{logging_parameter} is not a valid logging level')
            is_valid = False
            logging_level = logging.DEBUG
    except Exception as e:
        logger.warning(f'failed to parse logging parameter: {e}')
        is_valid = False
        logging_level = logging.DEBUG

    logger.debug(f'returning level: {logging_level} and status: {is_valid}')
    return logging_level, is_valid
