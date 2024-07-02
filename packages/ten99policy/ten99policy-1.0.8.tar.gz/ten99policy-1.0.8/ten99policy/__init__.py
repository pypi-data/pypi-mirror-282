from __future__ import absolute_import, division, print_function

# Configuration variables

client_id = None
api_base = "http://localhost:5000"
api_key = 't9sk_live_db68a311-e4b4-4ee8-b2d6-238bc97d83ed'
api_version = None
verify_ssl_certs = False
proxy = None
default_http_client = None
max_network_retries = 0
environment = 'sandbox'

# Set to either 'debug' or 'info', controls console logging
log = 'debug'

# API resources
from ten99policy.api_resources import *  # noqa
