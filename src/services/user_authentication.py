from specklepy.api.client import SpeckleClient
from specklepy.api.credentials import get_local_accounts, get_default_account
from specklepy.transports.server import ServerTransport
from specklepy.api import operations


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


sample_commit = sample_branch.commits.items[0]

server_transport = ServerTransport(stream_id=stream.id, client=client)

commit_obj = operations.receive(sample_commit.referencedObject, server_transport)

# Get properties
# sample_object = commit_obj["@Data"][0][0]
# sample_object_volume = sample_object.volume
# sample_object_area = sample_object.area

pass
