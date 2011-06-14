#!/usr/bin/env python

import sys
import logging

import lib
import config

def main(image_id, flavor_id, server_name):
    lib.connect(config.RS_USER, config.RS_KEY)
    image = lib.image_details({'id': int(image_id)})
    logging.info('Creating server from image %s' % (image['name'],))
    flavor = lib.flavor_details({'id': int(flavor_id)})
    logging.info('Creating server from flavor %s' % (flavor['name'],))
    data = lib.server_create(image, flavor, server_name)
    logging.info('  Id of new server: %d' % (data['id'],))
    logging.info('  Admin pass (IMPORTANT): %s' % (data['adminPass'],))
    logging.info('  Public IP: %s' % (', '.join(data['addresses']['public']),))
    logging.info('  Private IP: %s' % (', '.join(data['addresses']['private']),))


if __name__ == '__main__':
    logging.info('-'*60)
    logging.info('Start')
    if len(sys.argv) < 4:
        logging.error('Usage: server_create_from_image.py <imageId> <flavorId> <serverName>')
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
    logging.info('Stop')
    logging.info('-'*60)
