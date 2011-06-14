import logging
# INFO must be used or you won't see the response data
logging.basicConfig(level = logging.DEBUG,
                    format = '%(asctime)s - %(levelname)8s - %(message)s', 
                    datefmt = '%Y-%m-%d %H:%M:%S')


RS_USER = 'Your Rackspace user'
RS_KEY  = 'Your Rackspace api key'
