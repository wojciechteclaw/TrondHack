from distutils import debug
from specklepy.api.client import SpeckleClient
from specklepy.api.credentials import get_local_accounts, get_default_account
from specklepy.transports.server import ServerTransport
from specklepy.api import operations
from dotenv import load_dotenv
from os import environ, path, getenv
from specklepy.objects import Base

load_dotenv('../.env')

class UserAuthentication:
    
    def __init__(self) -> None:
        self.client = SpeckleClient(host="speckle.xyz")
    
    def get_client(self, client_name):
        all_accounts = get_local_accounts()
        
client = SpeckleClient(host="speckle.xyz")

# all_accounts = get_local_accounts()
# selected_account = next(acct for acct in all_accounts if client.url in acct.serverInfo.url)


account = get_default_account()
client.authenticate_with_account(account)


class BranchModel:
    def __init__(self, client, stream, branch):
        self.branch = branch
        self.client = client
        self.stream = stream


def get_branch_from_stream(client, stream_name, branch_name="main"):
    for stream in client.stream.list():
        if stream.name == stream_name:
            try:
                return BranchModel(
                                    client = client, 
                                    stream = stream, 
                                    branch = client.branch.get(stream.id, branch_name)
                                  )
            except Exception as e:
                print(e)

test_main_branch = get_branch_from_stream(client, "test branch")
materials_branch = get_branch_from_stream(client, "TrondHack_stage")
materials_bank_branch = get_branch_from_stream(client, "TrondHack_MaterialBank")



material_bank_last_commit = materials_bank_branch.branch.commits.items[0]
material_bank_server_transport = ServerTransport(stream_id=materials_bank_branch.stream.id, client=materials_bank_branch.client)
last_material_bank_commit = operations.receive(material_bank_last_commit.referencedObject, material_bank_server_transport)

last_commit_on_merging_branch = test_main_branch.branch.commits.items[0]
merging_branch_server_transport = ServerTransport(stream_id=test_main_branch.stream.id, client=test_main_branch.client)
mergin_branch_bank_commit = operations.receive(last_commit_on_merging_branch.referencedObject, merging_branch_server_transport)

# commit_obj["@Walls"][0]["parameters"]["LCA-sample"] = "12345"


class CommitMerger(Base):
    
    def __init__(self, original_commit, new_commit, **kwargs):
        super().__init__(**kwargs)
        self.original_commit = original_commit
        self.new_commit = new_commit
        
obj = CommitMerger(last_material_bank_commit, mergin_branch_bank_commit)

hash = operations.send(obj, [ServerTransport(stream_id=test_main_branch.stream.id, client=test_main_branch.client)])
commit_id = client.commit.create(stream_id=test_main_branch.stream.id,
                                 object_id=hash,
                                 message='This is a sample mergin commit')


pass
