from datetime import datetime
import json
from os import getenv
from specklepy.transports.server import ServerTransport
from specklepy.api import operations

from models.commit_merge_model import CommitMergeModel
from services.singleton import Singleton
from services.user_authorization_service import UserAuthorizationService
from models.branch_model import BranchModel


class StreamBranchManagerService(metaclass=Singleton):
    
    def __init__(self):
        self.stage_branch = None
        self.material_bank_branch = None
        self.client = None
    
    def register(self):
        self.client = UserAuthorizationService().client
        self.stage_branch = self.get_branch_model(getenv("STAGE_STREAM_NAME","TrondHack_stage"))
        self.material_bank_branch = self.get_branch_model(getenv("MATERIAL_BANK_STREAM_NAME","TrondHack_MaterialBank"))
    
    def get_branch_model(self, stream_name, branch_name="main"):
        for stream in UserAuthorizationService().client.stream.list():
            if stream.name == stream_name:
                return BranchModel(stream=stream, 
                                   branch=UserAuthorizationService().client.branch.get(stream.id, branch_name))
    
    def get_material_bank_branch_commit(self, commit_index=0):
        return self._get_commit(self.material_bank_branch, commit_index)
        
    def get_stage_branch_commit(self, commit_index=0):
        return self._get_commit(self.stage_branch, commit_index)
        
    def _get_commit(self, branch_model, commit_index):
        transport = ServerTransport(stream_id=branch_model.stream.id, client=UserAuthorizationService().client)
        try:
            commit_element = branch_model.branch.commits.items[commit_index]
            data = operations.receive(commit_element.referencedObject, transport)
            return data
        except KeyError as e:
            return None

    def merge_stage_with_bank(self):
        stage_data = self.get_stage_branch_commit(0)
        material_bank_data = self.get_material_bank_branch_commit(0)
        
        commit_merge_model = CommitMergeModel(material_bank_data, stage_data)
        object_to_send_id = operations.send(commit_merge_model, 
                                            [ServerTransport(self.material_bank_branch.stream.id, 
                                                             UserAuthorizationService().client)]
                                            )
        UserAuthorizationService().client.commit.create(stream_id=self.material_bank_branch.stream.id,
                                                        object_id=object_to_send_id,
                                                        message=StreamBranchManagerService.get_bank_commit_message()
                                                        )   
        return json.dumps('ok'), 200, {"Content-Type": "application/json"}
         
    @staticmethod
    def get_bank_commit_message():
        return f"Bank refres {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
