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

    def get_secret(self, mount_point, path) -> dict:
        try:
            secret = self.c.secrets.kv.v1.read_secret(mount_point=mount_point, path='data/{}'.format(path))['data']['data']
            return(secret)
        except:
            return(dict())
        
    def write_secret(self, mount_point, path, secret) -> bool:
        try:
            res = self.c.secrets.kv.v2.create_or_update_secret(mount_point=mount_point, path=path, secret=secret)
        except:
            return(False)
        if 'data' in res and 'created_time' in res['data']:
            return(True)
        else:
            return(False)