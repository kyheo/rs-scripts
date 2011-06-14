#!/usr/bin/env python

import sys
import logging

import lib
import config

def main(server_id, image_name):
    lib.connect(config.RS_USER, config.RS_KEY)
    server = lib.server_details({'id': int(server_id)})
    logging.info('Creating image from server %s' % (server['name'],))
    data = lib.image_create(server, image_name)
    logging.info('  Id of new image: %d' % (data['id'],))


if __name__ == '__main__':
    logging.info('-'*60)
    logging.info('Start')
    if len(sys.argv) < 3:
        logging.error('Usage: image_create_from_server.py <serverId> <imageName>')
    else:
        main(sys.argv[1], sys.argv[2])
    logging.info('Stop')
    logging.info('-'*60)
