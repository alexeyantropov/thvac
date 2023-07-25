import os
import sys
import logging
import hvac

url = os.environ.get('VAULT_ADDR')
root_token = os.environ.get('VAULT_DEV_ROOT_TOKEN_ID')
mountpoints = ['seek', 'destroy']
paths = ['flash', 'before', 'my', 'eyes']

if not url or not root_token:
    logging.critical('Env vars "url" or "token" are not set:  url: "{}", root_token: "{}"'.format(url, root_token))
    sys.exit(1)

c_tmp = hvac.Client(url, root_token)
production_token = c_tmp.auth.token.create(policies=['root'], ttl='1h')['auth']['client_token']

def main():
    c = hvac.Client(url, production_token)
    for i in range(len(mountpoints)):
        c.sys.enable_secrets_engine('kv', path=mountpoints[i], options={'version': 2})

if __name__ == '__main__':
    main()