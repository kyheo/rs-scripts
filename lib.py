import urllib2
import json
import logging

CONFIG = {}

class MultiMethodRequest(urllib2.Request):
    """Request class that extends urllib2.Request adding support for multiple
    request methods."""

    VALID_METHODS = ['GET', 'POST', 'DELETE', 'PUT', 'HEAD']

    def __init__(self, url, method=None, *args, **kwargs):
        if method is not None and method not in self.VALID_METHODS:
            method = None
        self.method = method
        urllib2.Request.__init__(self, url, *args, **kwargs)

    def get_method(self):
        if self.method is not None:
            return self.method
        return urllib2.Request.get_method(self)



def urlopen(url, data=None, method='GET', headers={}):
    """Extends urllib2.urlopen adding multi method support."""

    headers['Content-Type'] = 'application/json'
    if 'x-auth-token' in CONFIG:
        headers['X-Auth-Token'] = CONFIG['x-auth-token']

    logging.debug('urlopen %s' % (url,))

    req = MultiMethodRequest(url, method=method, headers=headers)
    res = urllib2.urlopen(req, json.dumps(data, 10))

    if 'x-auth-token' in CONFIG and res.getcode() == '401':
        logging.info('Unauthorized, re-login')
        connect()

    body = res.read()
    if body:
        body = json.loads(body)

    return res.getcode(), res.headers.dict, body


def connect(user, key_):
    code, headers, body = urlopen('http://auth.api.rackspacecloud.com/v1.0',
            headers={'X-Auth-User': user, 'X-Auth-Key': key_})

    if code == 204:
        logging.info('Logged in')
        CONFIG['x-server-management-url'] = headers['x-server-management-url']
        CONFIG['x-storage-url']           = headers['x-storage-url']
        CONFIG['x-cdn-management-url']    = headers['x-cdn-management-url']
        CONFIG['x-auth-token']            = headers['x-auth-token']
    else:
        raise Exception('Error login into the service.')


def image_create(server, image_name):
    url = '%s/images' % (CONFIG['x-server-management-url'])
    image = {'image': {'serverId': server['id'], 'name': image_name}}
    code, headers, body = urlopen(url, image, 'POST')
    if code != 202:
        logging.error('Error creating image')
        logging.error(code)
        logging.error(str(headers))
        logging.error(str(body))
        raise Exception(body)
    return body['image']


def image_delete(image):
    url = '%s/images/%d' % (CONFIG['x-server-management-url'], image['id'])
    code, headers, body = urlopen(url, method='DELETE')
    if code != 204:
        logging.error('Error deleting image')
        logging.error(code)
        logging.error(str(headers))
        logging.error(str(body))
        raise Exception(body)


def image_list():
    url = '%s/images/' % (CONFIG['x-server-management-url'],)
    code, headers, body = urlopen(url)
    if code not in [200, 203]:
        raise Exception('Error getting image lists')
    return body['images']


def image_details(image):
    url = '%s/images/%d' % (CONFIG['x-server-management-url'], image['id'])
    code, headers, body = urlopen(url)
    if code not in [200, 203]:
        raise Exception('Error getting image details')
    return body['image']


def flavor_list():
    url = '%s/flavors/' % (CONFIG['x-server-management-url'],)
    code, headers, body = urlopen(url)
    if code not in [200, 203]:
        raise Exception('Error getting flavor lists')
    return body['flavors']


def flavor_details(flavor):
    url = '%s/flavors/%d' % (CONFIG['x-server-management-url'], flavor['id'])
    code, headers, body = urlopen(url)
    if code not in [200, 203]:
        raise Exception('Error getting flavor details')
    return body['flavor']

    
def server_list():
    url = '%s/servers' % (CONFIG['x-server-management-url'],)
    code, headers, body = urlopen(url)
    if code not in [200, 203]:
        raise Exception('Error getting server lists')
    return body['servers']


def server_details(server):
    url = '%s/servers/%d' % (CONFIG['x-server-management-url'], server['id'])
    code, headers, body = urlopen(url)
    if code not in [200, 203]:
        raise Exception('Error getting server details')
    return body['server']


def server_create(image, flavor, server_name):
    url = '%s/servers' % (CONFIG['x-server-management-url'],)
    server = {'server': {'imageId': image['id'], 'name': server_name,
        'flavorId': flavor['id']}}
    code, headers, body = urlopen(url, server, 'POST')
    if code != 202:
        logging.error('Error creating server')
        logging.error(code)
        logging.error(str(headers))
        logging.error(str(body))
        raise Exception(body)
    return body['server']


def server_delete(server):
    url = '%s/servers/%d' % (CONFIG['x-server-management-url'], server['id'])
    code, headers, body = urlopen(url, method='DELETE')
    if code not in [202, 204]:
        logging.error('Error deleting server')
        logging.error(code)
        logging.error(str(headers))
        logging.error(str(body))
        raise Exception(body)
