from utils.config_parser import Parameters
from utils.request_util import *
from utils.html_parser_util import *
import logging

logger = logging.getLogger('whisky_scaper.main')

#requests whiskybrokers html content
response = get_response_from_url(Parameters.whiskybroker_base_url)
html = parse_response_to_text(response)

#parse html to usefull data
