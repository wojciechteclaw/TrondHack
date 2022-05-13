from os import getenv
from specklepy.api.client import SpeckleClient
from specklepy.api.credentials import get_default_account

from service.singleton import Singleton


class UserAuthorizationService(metaclass=Singleton):
    
    def __init__(self):
        self._host = getenv("SPECKLE_HOST", "speckle.xyz")
        self._client = None
        
    def register(self):
        client = SpeckleClient(self._host)
        account = get_default_account()
        client.authenticate_with_account(account)
        self._client = client

    @property
    def client(self):
        return self._client
