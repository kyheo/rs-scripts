#!/usr/bin/env python

import sys
import logging

import lib
import config

def main(server_id):
    lib.connect(config.RS_USER, config.RS_KEY)
    server = lib.server_details({'id': int(server_id)})
    logging.info(server)


if __name__ == '__main__':
    logging.info('-'*60)
    logging.info('Start')
    if len(sys.argv) < 2:
        logging.error('Usage: server_details.py <serverId>')
    else:
        main(sys.argv[1])
    logging.info('Stop')
    logging.info('-'*60)
