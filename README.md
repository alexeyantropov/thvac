<!-- TOC -->

- [thvac](#thvac)
- [How to use](#how-to-use)
    - [Class Clienturl, token](#class-clienturl-token)
    - [Client.token_renew](#clienttoken_renew)
    - [Client.secret_getmount_point, path](#clientsecret_getmount_point-path)
    - [Client.secret_writemount_point, path, secret](#clientsecret_writemount_point-path-secret)
    - [Client.mount_list](#clientmount_list)
    - [Client.mount_createmount_point](#clientmount_createmount_point)
- [WTF?](#wtf)
- [Developing and testing environment](#developing-and-testing-environment)

<!-- /TOC -->

# thvac
The Teensy Hvac is a wrapper for the hvac module giving a simpler interface. Thvac works only with token auth and kv2 secret engine.

# How to use
```
import thvac

client = thvac.Client('https://vault:8200', 'token')

if not mount_create('mountpoint'):
    raise Exception('Oops')

client.secret_write('mountpoint', 'path/to', {'password': 'fish})

if client.secret_get('mountpoint', 'path/to')['password] == 'fish':
    client.secret_write('mountpoint', 'path/to', {'password': 'herring', 'fish': 'was here'})

```
## Class Client(url, token)
Creates a new client.

## Client.token_renew()
Renews the client token.

Return: bool.

## Client.secret_get(mount_point, path)

Returns: dict() with the secret data. If smth is wrong it always returns an empty dict().

## Client.secret_write(mount_point, path, secret)
Secret should be a dict().

Returns: bool. False only if an error has happended.

## Client.mount_list()
Lists all mountpoints list.

Returns: set().

## Client.mount_create(mount_point)
Creates a new kv2 mountpoint.

Returns: bool, it always is True if there isn't any error.

# WTF?
I use [hvac](https://github.com/hvac/hvac) in my everyday work and the official client basically provides a lot of bricks for building youown local client for your tasks and evironment. And it's OK.

However I recon there is a little problem and I want to code a tiny client using hvac (not bare Vault API) with a simplier to use interface based on my expirience with Vault and hvac.

# Developing and testing environment
All assets and docs for developing and testing in the 'develop' folder. It uses docker-compose, [the Vault docker image](https://hub.docker.com/_/vault), and [the Python image](https://hub.docker.com/_/python).

It is runned and developed on python 3.9 but I sure that another python version aren't a problem.
