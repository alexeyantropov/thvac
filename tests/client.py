import sys

sys.path.append('.')
sys.path.append('./src')
sys.path.append('./develop')

from test_data import *
import src as thvac

okay_client = thvac.Client(url, production_token)
broken_client = thvac.Client(url, 'invalid token')
mountpoint = mountpoints[0]
path = 'test_write_secret_1'
secret_1 = {'k': 'v'}

def test_init_1():
    assert okay_client.is_authenticated == True

def test_init_2():
    assert broken_client.is_authenticated == False

def test_token_renew_1():
    assert okay_client.token_renew() == True

def test_token_renew_2():
    assert broken_client.token_renew() == False

def test_write_secret_1():
    assert okay_client.write_secret(mountpoint, path, secret_1) == True

def test_write_secret_2():
    assert broken_client.write_secret(1, 2, 3) == False

def test_get_secret_1():
    assert okay_client.get_secret(mountpoint, path) == secret_1

def test_get_secret_2():
    assert okay_client.get_secret(mountpoint, 'not-existen-secret') == dict()
