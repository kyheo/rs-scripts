#!/usr/bin/env python

import sys
import logging

import lib
import config

def main(flavor_id):
    lib.connect(config.RS_USER, config.RS_KEY)
    flavor = lib.flavor_details({'id': int(flavor_id)})
    logging.info(flavor)


if __name__ == '__main__':
    logging.info('-'*60)
    logging.info('Start')
    if len(sys.argv) < 2:
        logging.error('Usage: flavor_details.py <flavorId>')
    else:
        main(sys.argv[1])
    logging.info('Stop')
    logging.info('-'*60)
