#!/usr/bin/env python

import sys
import logging

import lib
import config

def main(image_id):
    lib.connect(config.RS_USER, config.RS_KEY)
    lib.image_delete({'id': int(image_id)})


if __name__ == '__main__':
    logging.info('-'*60)
    logging.info('Start')
    if len(sys.argv) < 2:
        logging.error('Usage: image_delete.py <imageId>')
    else:
        main(sys.argv[1])
    logging.info('Stop')
    logging.info('-'*60)
