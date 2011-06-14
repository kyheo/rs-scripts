#!/usr/bin/env python

import sys
import logging

import lib
import config

def main(server_name, image_name_prefix):
    lib.connect(config.RS_USER, config.RS_KEY)
    servers = lib.server_list()
    for server in servers:
        if server['name'].startswith(server_name):
            image_name = '%s%s' % (image_name_prefix, server['name'])
            logging.info('Creating image from server %s with name %s' %
                    (server['name'], image_name))
            data = lib.image_create(server, image_name_prefix)
            logging.info('  Id of new image: %d' % (data['id'],))



if __name__ == '__main__':
    logging.info('-'*60)
    logging.info('Start')
    if len(sys.argv) < 3:
        logging.error('Usage: image_create_from_filtered_servers.py <serverName> <imageNamePrefix>')
        logging.error('       use "" as imageNamePrefix if no prefix is needed')
    else:
        main(sys.argv[1], sys.argv[2])
    logging.info('Stop')
    logging.info('-'*60)
