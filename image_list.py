#!/usr/bin/env python

import sys
import logging

import lib
import config

def main():
    lib.connect(config.RS_USER, config.RS_KEY)
    images = lib.image_list()
    logging.info('id - name - status - progress')
    for image in images:
        logging.info(image)


if __name__ == '__main__':
    logging.info('-'*60)
    logging.info('Start')
    main()
    logging.info('Stop')
    logging.info('-'*60)
