import hvac

class Client:
    def __init__(self, url: str, token: str):
        self.c = hvac.Client(url, token)
        self.token = token
        if self.c.is_authenticated():
            self.is_authenticated = True
        else:
            self.is_authenticated = False
    
    def token_renew(self) -> bool:
        try:
            self.c.renew_token(self.token)
            return(True)
        except:
            return(False)

    def secret_get(self, mount_point, path) -> dict:
        try:
            secret = self.c.secrets.kv.v1.read_secret(mount_point=mount_point, path='data/{}'.format(path))['data']['data']
            return(secret)
        except:
            return(dict())

    def secret_write(self, mount_point, path, secret) -> bool:
        """ A little check
        Are an old version of a secret and the new one the same?
        If they are the same, the method does nothin and returns True.
        The check is neccecary to avoid dummy version bumping in kv2 storage.
        """
        secret_old = self.secret_get(mount_point, path)
        if secret == secret_old:
            return(True)
        
        try:
            res = self.c.secrets.kv.v2.create_or_update_secret(mount_point=mount_point, path=path, secret=secret)
        except:
            return(False)
        
        if 'data' in res and 'created_time' in res['data']:
            return(True)
        else:
            return(False)
        
    def mount_list(self) -> set:
        # The method returns set() to provide lookups for O(1) time.
        try:
            res = self.c.sys.list_mounted_secrets_engines()['data'] # {'foo/': {...}, 'bar/': {...}}
            tmp = [ x[0:len(x)-1] for x in res.keys() ] # 'foo/' -> 'foo'
            return(set(tmp))
        except:
            return(set())
    
    def mount_create(self, path) -> bool:
        """
        The same check as in the secret_write() method.
        """
        mount_list = self.mount_list()
        if path in mount_list:
            return(True)
        
        try:
            self.c.sys.enable_secrets_engine('kv', path=path, options={'version': 2})
            return(True)
        except:
            return(False)