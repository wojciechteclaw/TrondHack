from mediatr import Mediator

from commands.merge_stage_with_bank_command import MergeStageWithBankCommand
from services.stream_branch_manager_service import StreamBranchManagerService


@Mediator.handler
class MergeStageWithBankCommandHandler:
    
    def handle(self, command: MergeStageWithBankCommand):
        return StreamBranchManagerService().merge_stage_with_bank()