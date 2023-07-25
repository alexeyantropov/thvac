import os
import sys
import logging
import hvac

url = os.environ.get('VAULT_ADDR')
root_token = os.environ.get('VAULT_DEV_ROOT_TOKEN_ID')
mountpoints = ['first_secrets', 'second_secrets']
paths = ['flash', 'before', 'my', 'eyes']
secrets = [
    {'key': 'value'},
    {'foo': 'Hello', 'bar': 'World'},
    {'user': 'lame', 'password': 'fish', 'db': 'mysql', 'host': '127.0.0.2'},
    {'another': 'one', 'bites': 'the dust'},
    {'he': 'had', 'no': 'money'},
    {'no': 'good', 'at': 'home'}
]

if not url or not root_token:
    logging.critical('Env vars "url" or "token" are not set:  url: "{}", root_token: "{}"'.format(url, root_token))
    sys.exit(1)

if len(paths) > len(secrets):
    logging.critical('It needs more secrets!')
    sys.exit(1)

c_tmp = hvac.Client(url, root_token)
production_token = c_tmp.auth.token.create(policies=['root'], ttl='1h')['auth']['client_token']

def main():
    c = hvac.Client(url, production_token)
    for i in range(len(mountpoints)):
        c.sys.enable_secrets_engine('kv', path=mountpoints[i], options={'version': 2})
        for j in range(len(paths)):
            for k in range(0,2):
                c.secrets.kv.v2.create_or_update_secret(mount_point=mountpoints[i], path=paths[j], secret=secrets[j+k])

if __name__ == '__main__':
    main()