#!/usr/bin/env python3

import argparse

from utils.whiskybroker_util import Whiskybroker_scraper
from utils.config_parser import Parameters


scraper = Whiskybroker_scraper(Parameters.whiskybroker_base_url)
print(scraper.scrape_all_pages())