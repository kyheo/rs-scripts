#!/usr/bin/env python

import sys
import logging

import lib
import config

def main():
    lib.connect(config.RS_USER, config.RS_KEY)
    servers = lib.server_list()
    for server in servers:
        logging.info(server)


if __name__ == '__main__':
    logging.info('-'*60)
    logging.info('Start')
    main()
    logging.info('Stop')
    logging.info('-'*60)
