#!/usr/bin/env python

import sys
import logging

import lib
import config

def main(image_id):
    lib.connect(config.RS_USER, config.RS_KEY)
    image = lib.image_details({'id': int(image_id)})
    logging.info(image)


if __name__ == '__main__':
    logging.info('-'*60)
    logging.info('Start')
    if len(sys.argv) < 2:
        logging.error('Usage: image_details.py <imageId>')
    else:
        main(sys.argv[1])
    logging.info('Stop')
    logging.info('-'*60)
