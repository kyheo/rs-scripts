#!/usr/bin/env python

import sys
import logging

import lib
import config

def main():
    lib.connect(config.RS_USER, config.RS_KEY)
    flavors = lib.flavor_list()
    for flavor in flavors:
        logging.info(flavor)


if __name__ == '__main__':
    logging.info('-'*60)
    logging.info('Start')
    main()
    logging.info('Stop')
    logging.info('-'*60)
