import logging

from dataclasses import dataclass
from os.path import abspath, join
from pathlib import Path

from utils import logger
from utils.json_util import load_json_file
from utils.logging_util import get_logging_level_from_parameter

logger = logging.getLogger('whisky_tracker.config_parser')


#config fields dict with key : value type
REQUIRED_CONFIG_FIELDS = {"whiskybroker base url" : str, "email address" : str, "data dir": str, "general logging level" :str}
OPTONAL_CONFIG_FIELDS = {}


def get_missing_config_fields(config_dict):
    return set(REQUIRED_CONFIG_FIELDS) - set(config_dict)

def is_correct_value_type(parameter, type):
    return isinstance(parameter, type)

#TODO: Not the most pytohnic, and logical code.
def is_valid_config(config_dict):
    is_valid = False
    config_fields = list(config_dict.keys())
    if config_fields == list(REQUIRED_CONFIG_FIELDS.keys()):
        logging.debug('all config fields where in the config dict')
        is_valid = True
        for parameter, value in config_dict.items():
            if not is_correct_value_type(value, REQUIRED_CONFIG_FIELDS[parameter]):
                is_valid = False
                break
    return is_valid

@dataclass
class Parameters:
    program_dir = Path(abspath(__file__)).parents[1]
    config_dir = 'config'
    config_name = 'default_config.json'
    config_path = join(program_dir, config_dir, config_name)

    #try to load the config file
    try:
        #load json file here
        config_dict = load_json_file(config_path)
    except FileNotFoundError:
        logger.critical(f'config file was not found at: {config_path}')
        exit(1)

    except Exception as e:
        logger.critical(f'failed to load config file: {e}')
        exit(1)

    if is_valid_config(config_dict):
        #set all parameters here
        root_dir = Path(abspath(__file__)).parents[1]
        whiskybroker_base_url = config_dict['whiskybroker base url']
        email_address = config_dict['email address']
        data_dir = join(root_dir, config_dict['data dir'])


        logging_level, status = get_logging_level_from_parameter(config_dict['general logging level'])
        #TODO: maybe change the below logging to debug
        logging.info(f'logging level parsing status: {status}')
        logger.info(f'setting general logging level to: {logging_level}')
        logger.setLevel(logging_level)

    else:
        #TODO: check why the config dict was not valid, and return any missing keys/wrong values
        logger.critical(f'config file contained something wrong...')
        exit(1)
