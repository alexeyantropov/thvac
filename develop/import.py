import os
import sys
import logging
import hvac

url = os.environ.get('VAULT_ADDR')
port = os.environ.get('VAULT_PORT')
token = os.environ.get('VAULT_DEV_ROOT_TOKEN_ID')
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

if not url or not token:
    logging.critical('Env vars "url" or "port" or "token" are not set:  url: "{}", port: "{}", token: "{}"'.format(url, port, token))
    sys.exit(1)

if len(paths) > len(secrets):
    logging.critical('It needs more secrets!')
    sys.exit(1)

def main():
    c = hvac.Client('{}:{}'.format(url, port), token)
    for i in range(len(mountpoints)):
        c.sys.enable_secrets_engine('kv', path=mountpoints[i], options={'version': 2})
        for j in range(len(paths)):
            for k in range(0,2):
                c.secrets.kv.v2.create_or_update_secret(mount_point=mountpoints[i], path=paths[j], secret=secrets[j+k])

if __name__ == '__main__':
    main()