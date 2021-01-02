import logging

# create base logger with 'whisky_tracker'
logger = logging.getLogger('whisky_tracker')
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
fh = logging.FileHandler('whisky_tracker.log')
#fh.setLevel(logging.DEBUG)

# create console handler, can also give it a specific logging level
ch = logging.StreamHandler()
#ch.setLevel(logging.DEBUG)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

#optionally: set the logging level globally
logger.setLevel(logging.DEBUG)