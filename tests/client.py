
'''
A little convention about test names: test_(1)___(2), where:
1 - Name of a functionality or a method;
2 - A clarification or a detail describes the test.
'''

import sys
import time

sys.path.append('.')
import develop
import src as thvac
 
okay_client = thvac.Client(develop.url, develop.production_token)
broken_client = thvac.Client(develop.url, 'invalid token')

mountpoint = develop.mountpoints[0]
mountpoint_dynamic = 'mount_{}'.format(time.time())
path = develop.paths[0]

secret_static_1 = {'k': 'v'}
secret_dynamic_1 = {'k': str(time.time())}

# Init
def test_init___okay_client():
    assert okay_client.is_authenticated == True

def test_init___broken_client():
    assert broken_client.is_authenticated == False

# token_renew
def test_token_renew___okay_client():
    assert okay_client.token_renew() == True

def test_token_renew___broken_client():
    assert broken_client.token_renew() == False

# secret_write
def test_secret_write___static_1():
    okay_client.secret_write(mountpoint, path, secret_static_1)
    assert okay_client.secret_write(mountpoint, path, secret_static_1) == True

def test_secret_write___dymanic_1():
    assert okay_client.secret_write(mountpoint, path, secret_dynamic_1) == True

def test_secret_write___wrong_path():
    assert okay_client.secret_write('mountpoint-doesnt-exist', 'wrong-path', secret_static_1) == False

# secret_get
def test_secret_get___existen___secret_dynamic_1():
    assert okay_client.secret_get(mountpoint, path) == secret_dynamic_1

def test_secret_get___not_existen():
    assert okay_client.secret_get(mountpoint, 'not-existen-secret') == dict()

# mount_create
def test_mount_create___static_1():
    okay_client.mount_create(mountpoint)
    assert okay_client.mount_create(mountpoint) == True
    
def test_mount_create___dynamic_1():
    assert okay_client.mount_create(mountpoint_dynamic) == True

def test_mount_create___broken_client():
    assert broken_client.mount_create(mountpoint_dynamic) == False

# mount_list
def test_mount_list___dynamic_1():
    assert mountpoint_dynamic in okay_client.mount_list()

def test_mount_list___broken_client():
    assert broken_client.mount_list() == set()