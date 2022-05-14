from specklepy.api.client import SpeckleClient
from specklepy.api.credentials import get_local_accounts, get_default_account


# class UserAuthentication:
    
#     def __init__(self) -> None:
#         self.client = SpeckleClient(host="speckle.xyz")
    
#     def get_client(self, client_name):
#         all_accounts = get_local_accounts()
        
client = SpeckleClient(host="speckle.xyz")

# all_accounts = get_local_accounts()
# selected_account = next(acct for acct in all_accounts if client.url in acct.serverInfo.url)


account = get_default_account()
client.authenticate_with_account(account)

stream = client.stream.list()[0]

sample_branch = client.branch.get(stream.id, 'main')


pass
